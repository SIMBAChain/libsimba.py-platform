import unittest
from unittest.mock import patch

from libsimba.simba import Simba


class TestSimba(unittest.TestCase):
    def setUp(self):
        self.simba = Simba()
        patcher_send = patch("libsimba.simba_request.SimbaRequest.send")
        patcher_init = patch("libsimba.simba_request.SimbaRequest.__init__")
        self.addCleanup(patcher_send.stop)
        self.addCleanup(patcher_init.stop)
        self.mock_send = patcher_send.start()
        self.mock_init = patcher_init.start()
        self.mock_init.return_value = None

    def test_submit_transaction_by_address(self):
        resp = self.simba.submit_transaction_by_address(
            "app_id",
            "contract",
            "identifier",
            "method",
            {"key": "value"},
        )
        self.mock_send.assert_called_once_with(headers={}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/contract/contract/address/identifier/method/', {}, method='POST')

    def test_submit_transaction_by_address_with_params(self):
        resp = self.simba.submit_transaction_by_address(
            "app_id",
            "contract",
            "identifier",
            "method",
            {"key": "value"},
            query_args={"bob": "boby"},
            sender_address="0x1773",
        )
        self.mock_send.assert_called_once_with(
            headers={'txn-sender': '0x1773'}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/contract/contract/address/identifier/method/', {"bob": "boby"}, method='POST')

    def test_submit_transaction_by_asset(self):
        resp = self.simba.submit_transaction_by_asset(
            "app_id",
            "contract",
            "identifier",
            "method",
            {"key": "value"},
        )
        self.mock_send.assert_called_once_with(headers={}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/contract/contract/asset/identifier/method/', {}, method='POST')

    def test_submit_transaction_by_asset_with_params(self):
        resp = self.simba.submit_transaction_by_asset(
            "app_id",
            "contract",
            "identifier",
            "method",
            {"key": "value"},
            query_args={"bob": "boby"},
            sender_address="0x1773",
        )
        self.mock_send.assert_called_once_with(
            headers={'txn-sender': '0x1773'}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/contract/contract/asset/identifier/method/', {"bob": "boby"}, method='POST')

    def test_submit_contract_method(self):
        resp = self.simba.submit_contract_method(
            "app_id",
            "contract",
            "method",
            {"key": "value"},
        )
        self.mock_send.assert_called_once_with(headers={}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/contract/contract/method/', {}, method='POST')

    def test_submit_contract_method_with_params(self):
        resp = self.simba.submit_contract_method(
            "app_id",
            "contract",
            "method",
            {"key": "value"},
            query_args={"bob": "boby"},
            sender_address="0x1773",
        )
        self.mock_send.assert_called_once_with(
            headers={'txn-sender': '0x1773'}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/contract/contract/method/', {"bob": "boby"}, method='POST')

    def test_submit_transaction_by_address_async(self):
        resp = self.simba.submit_transaction_by_address_async(
            "app_id",
            "contract",
            "identifier",
            "method",
            {"key": "value"},
        )
        self.mock_send.assert_called_once_with(headers={}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/async/contract/contract/address/identifier/method/', {}, method='POST')

    def test_submit_transaction_by_address_async_with_params(self):
        resp = self.simba.submit_transaction_by_address_async(
            "app_id",
            "contract",
            "identifier",
            "method",
            {"key": "value"},
            query_args={"bob": "boby"},
            sender_address="0x1773",
        )
        self.mock_send.assert_called_once_with(
            headers={'txn-sender': '0x1773'}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/async/contract/contract/address/identifier/method/', {"bob": "boby"}, method='POST')

    def test_submit_transaction_by_asset_async(self):
        resp = self.simba.submit_transaction_by_asset_async(
            "app_id",
            "contract",
            "identifier",
            "method",
            {"key": "value"},
        )
        self.mock_send.assert_called_once_with(headers={}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/async/contract/contract/asset/identifier/method/', {}, method='POST')

    def test_submit_transaction_by_asset_async_with_params(self):
        resp = self.simba.submit_transaction_by_asset_async(
            "app_id",
            "contract",
            "identifier",
            "method",
            {"key": "value"},
            query_args={"bob": "boby"},
            sender_address="0x1773",
        )
        self.mock_send.assert_called_once_with(
            headers={'txn-sender': '0x1773'}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/async/contract/contract/asset/identifier/method/', {"bob": "boby"}, method='POST')

    def test_submit_contract_method_async(self):
        resp = self.simba.submit_contract_method_async(
            "app_id",
            "contract",
            "method",
            {"key": "value"},
        )
        self.mock_send.assert_called_once_with(headers={}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/async/contract/contract/method/', {}, method='POST')

    def test_submit_contract_method_async_with_params(self):
        resp = self.simba.submit_contract_method_async(
            "app_id",
            "contract",
            "method",
            {"key": "value"},
            query_args={"bob": "boby"},
            sender_address="0x1773",
        )
        self.mock_send.assert_called_once_with(
            headers={'txn-sender': '0x1773'}, json_payload={"key": "value"})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/async/contract/contract/method/', {"bob": "boby"}, method='POST')

    def test_create_contract_instance(self):
        resp = self.simba.create_contract_instance(
            "app_id",
            "contract",
        )
        self.mock_send.assert_called_once_with(headers={})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/new/contract/', {}, method='POST')

    def test_create_contract_instance_with_params(self):
        resp = self.simba.create_contract_instance(
            "app_id",
            "contract",
            query_args={"bob": "boby"},
            sender_address="0x1773",
        )
        self.mock_send.assert_called_once_with(
            headers={'txn-sender': '0x1773'})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/new/contract/', {"bob": "boby"}, method='POST')

    def test_submit_signed_transaction(self):
        resp = self.simba.submit_signed_transaction(
            "app_id",
            "tnx-id",
            {"txn": "data"},
        )
        self.mock_send.assert_called_once_with(json_payload={'transaction': {'txn': 'data'}})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/transactions/tnx-id/', {}, method='POST')

    def test_submit_signed_transaction_with_params(self):
        resp = self.simba.submit_signed_transaction(
            "app_id",
            "tnx-id",
            {"txn": "data"},
            query_args={"bob": "boby"},
        )
        self.mock_send.assert_called_once_with(json_payload={'transaction': {'txn': 'data'}})
        self.mock_init.assert_called_once_with(
            '/v2/apps/app_id/transactions/tnx-id/', {'bob': 'boby'}, method='POST')



