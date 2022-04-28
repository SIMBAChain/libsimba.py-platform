import unittest

from libsimba.decorators import auth_required
from libsimba.simba_request import SimbaRequest


class MockClass:
    @auth_required
    def test_func(self, headers: dict = None, payload=None):
        return headers, payload


class TestAuthRequired(unittest.TestCase):
    def test_auth_required_no_params(self):
        resp = MockClass().test_func()
        self.assertEqual(resp, ({"Authorization": "Bearer None"}, None))

    def test_auth_required_headers(self):
        resp = MockClass().test_func(headers={"bob": "test"}, payload={})
        self.assertEqual(resp, ({"bob": "test", "Authorization": "Bearer None"}, {}))
