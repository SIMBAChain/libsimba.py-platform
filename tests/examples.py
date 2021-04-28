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
