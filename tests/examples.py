import json
import os
import unittest
import logging

from libsimba.settings import BASE_API_URL, TEST_APP, TEST_CONTRACT, TEST_INPUTS, TEST_METHOD
from libsimba.simba import Simba

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class TestSEP(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.simba = Simba(BASE_API_URL)

    def test_001(self):
        """
        Submit some test data from a test app
        """

        contract = self.simba.get_contract(TEST_APP, TEST_CONTRACT)
        log.info('{} :: {} :: {}'.format(BASE_API_URL, TEST_APP, TEST_CONTRACT))

        r = contract.submit_method(TEST_METHOD, TEST_INPUTS)
        log.info(r.text)
        assert (200 <= r.status_code <= 299)
        log.info(r.json())

    def test_002(self):
        """
        Query some test data from a test app
        """
        contract = self.simba.get_contract(TEST_APP, TEST_CONTRACT)
        log.info('{} :: {} :: {}'.format(BASE_API_URL, TEST_APP, TEST_CONTRACT))

        r = contract.query_method(TEST_METHOD)
        assert (200 <= r.status_code <= 299)
        log.info(r.json())

    def test_003(self):
        """
        Get whoami info for this authenticated user
        """
        r = self.simba.whoami()
        assert (200 <= r.status_code <= 299)
        log.info(r.json())

    def test_004(self):
        """
        Submit file to contract
        """

        TEST_APP = 'compBatch'
        TEST_CONTRACT = 'ComponentBatch'
        TEST_METHOD = 'request_for_initialization'
        TEST_INPUTS = {
            '__batch_number': 'abcdef2',
            'datetime': '5764253'
        }

        f1 = open('./data/file1.txt', 'r')
        TEST_FILES = [
            ('file1.txt', f1)
        ]

        contract = self.simba.get_contract(TEST_APP, TEST_CONTRACT)
        r = contract.submit_contract_method_with_files(TEST_METHOD, TEST_INPUTS, TEST_FILES)

        f1.close()

        res = r.json()
        log.info(res)
        assert (200 <= r.status_code <= 299)

        assert 'inputs' in res
        assert '_bundleHash' in res['inputs']
        assert res['inputs']['_bundleHash'] != ''


