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
        self.policy=json.loads((ROOT/'config/curation.json').read_text())
        self.record=copy.deepcopy(json.loads((ROOT/'data/resources.json').read_text())[0])
    def errors(self):
        return validator.validate_resources([self.record],self.policy,date(2026,9,11))
    def test_real_records_pass(self):
        self.assertEqual(validator.validate(ROOT),[])
    def test_runtime_claim_needs_actual_test(self):
        self.record['verification']='runtime-tested'
        self.assertTrue(any('without test evidence' in x for x in self.errors()))
    def test_old_source_cannot_be_relabelled_recent(self):
        self.record['freshness']='recent'
        self.assertTrue(any('unsupported recent' in x for x in self.errors()))
    def test_unknown_dates_do_not_make_a_new_article(self):
        self.record.update(freshness='recent',published_at=None,substantively_updated_at=None)
        self.assertTrue(any('unsupported recent' in x for x in self.errors()))
    def test_inflated_total_does_not_override_evidence(self):
        self.record['score']['evidence']=1
        self.record['score_total']=99
        self.assertTrue(any('threshold' in x for x in self.errors()))
    def test_auth_and_throttling_are_not_dead_links(self):
        self.assertEqual(audit.classify(403),'blocked-or-auth-required')
        self.assertEqual(audit.classify(429),'rate-limited')
        self.assertEqual(audit.classify(404),'missing-recheck-required')
    def test_service_docs_cannot_be_counted_as_main_re(self):
        self.record['listing_file']='README.md'
        self.assertTrue(any('wrong listing' in x for x in self.errors()))
    def test_core_needs_inspected_artifact(self):
        self.record.update(editorial_role='re-tool',listing_file='README.md')
        self.assertTrue(any('core RE needs' in x for x in self.errors()))
    def test_old_case_can_remain_without_a_current_tool_claim(self):
        case=next(x for x in json.loads((ROOT/'data/resources.json').read_text())
                  if x['id']=='akamai-habr-interpreter')
        self.assertEqual(validator.validate_resources([case],self.policy,date(2026,9,12)),[])
        case=copy.deepcopy(case)
        case['freshness']='recent'
        self.assertTrue(any('unsupported recent' in x for x in
            validator.validate_resources([case],self.policy,date(2026,9,12))))
    def test_undated_snapshot_needs_immutable_source(self):
        case=copy.deepcopy(next(x for x in json.loads((ROOT/'data/resources.json').read_text())
                              if x['id']=='akamai-bmp'))
        case['re_artifact_urls']=[case['url']]
        case['evidence_urls'].append(case['url'])
        self.assertTrue(any('immutable artifact' in x for x in
            validator.validate_resources([case],self.policy,date(2026,9,12))))
    def test_snapshot_does_not_certify_obsolete_software(self):
        case=copy.deepcopy(next(x for x in json.loads((ROOT/'data/resources.json').read_text())
                              if x['id']=='akamai-bmp'))
        case['kind']='software'
        self.assertTrue(any('bounded research' in x for x in
            validator.validate_resources([case],self.policy,date(2026,9,12))))

if __name__=='__main__': unittest.main()
