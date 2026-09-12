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

if __name__=='__main__': unittest.main()
