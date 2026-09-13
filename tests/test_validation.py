import copy
import importlib.util
import json
import unittest
from datetime import date
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value
validator=module('validate');audit=module('audit_links')

class EditorialGates(unittest.TestCase):
    def setUp(self):
        self.policy=json.loads((ROOT/'config/curation.json').read_text(encoding='utf-8'))
        self.record=copy.deepcopy(json.loads((ROOT/'data/resources.json').read_text(encoding='utf-8'))[0])
    def errors(self):
        return validator.validate_resources([self.record],self.policy,date(2026,9,13))
    def test_real_records_pass(self):
        self.assertEqual(validator.validate(ROOT),[])
    def test_runtime_claim_needs_actual_test(self):
        self.record['verification']='runtime-tested'
        self.assertTrue(any('without test evidence' in x for x in self.errors()))
    def test_old_source_cannot_be_relabelled_recent(self):
        self.record['freshness']='recent'
        self.assertTrue(any('unsupported recent' in x for x in self.errors()))
    def test_inflated_total_does_not_override_evidence(self):
        self.record['score']['evidence']=1
        self.record['score_total']=99
        self.assertTrue(any('threshold' in x for x in self.errors()))
    def test_auth_and_throttling_are_not_dead_links(self):
        self.assertEqual(audit.classify(403),'blocked-or-auth-required')
        self.assertEqual(audit.classify(429),'rate-limited')
        self.assertEqual(audit.classify(404),'missing-recheck-required')
    def test_supporting_needs_re_use_and_excludes_integration(self):
        self.record.pop('re_use', None)
        self.assertTrue(any('concrete RE use' in x for x in self.errors()))
        self.record['re_use']='Widget integration'
        self.record['kind']='service-docs'
        self.assertTrue(any('standalone service integration' in x for x in self.errors()))
    def test_core_needs_inspected_artifact(self):
        self.record.update(editorial_role='re-tool',listing_file='README.md')
        self.assertTrue(any('core RE needs' in x for x in self.errors()))
    def test_snapshot_requires_scope_method_and_evidence(self):
        self.record['freshness']='snapshot'
        self.assertTrue(any('snapshot needs' in x for x in self.errors()))
        self.record.update(historical_scope='Study of an explicitly captured 2020 sample',
                           snapshot_version='Fixture release 2020.01',
                           method_value='Teaches how to inspect a verifier boundary',
                           snapshot_artifact_urls=[self.record['evidence_urls'][0]])
        self.record['published_at']='2020-01-01'
        self.assertEqual(self.errors(),[])
        self.record.pop('snapshot_version')
        self.assertTrue(any('version/artifact identifier' in x for x in self.errors()))
        self.record['snapshot_version']='Fixture release 2020.01'
        self.record['snapshot_artifact_urls']=['https://example.com/uninspected']
        self.assertTrue(any('inspected artifact' in x for x in self.errors()))
    def test_useful_boundary_does_not_relax_evidence_gate(self):
        self.record['score']={k:4 for k in self.policy['weights']}
        self.record['score_total']=80
        self.assertEqual(self.errors(),[])
        self.record['score']['evidence']=3
        self.record['score']['scope']=5
        self.assertTrue(any('threshold' in x for x in self.errors()))
    def test_quality_tier_boundaries(self):
        for value, expected in [(69.9,'deferred'),(70,'watchlist'),(79.9,'watchlist'),
                                (80,'useful'),(84.5,'useful'),(85,'gold'),(100,'gold')]:
            self.assertEqual(validator.quality_tier(value,self.policy),expected)
    def test_snapshot_cannot_claim_current_operation(self):
        self.record.update(freshness='snapshot',historical_scope='Old sample',
                           method_value='Inspectable method',
                           snapshot_artifact_urls=[self.record['evidence_urls'][0]],
                           description='A working implementation')
        self.assertTrue(any('snapshot cannot imply' in x for x in self.errors()))

if __name__=='__main__': unittest.main()
