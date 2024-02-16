import re
import unittest

from hummingbot.connector.derivative._100x_perpetual._100x_perpetual_auth import Class100xPerpetualAuth


class Class100xPerpetualAuthTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.network_address = "0x836eE2b55d173245832995082a8600709c38D099"
        self.private_key = "13e56ca9cceebf1f33065c2c5376ab38570a114bc1b003b60d838f92be9d7930"  # noqa: mock
        self.auth_instance = Class100xPerpetualAuth(network_address=self.network_address, private_key=self.private_key)

    def test_login_message_generation(self):
        login_message = self.auth_instance._generate_eip_712_login_message()

        assert 'domain' in login_message, "The 'domain' field is missing"
        assert 'message' in login_message, "The 'message' field is missing"
        assert 'primaryType' in login_message, "The 'primaryType' field is missing"
        assert 'types' in login_message, "The 'types' field is missing"
        domain = login_message['domain']
        assert isinstance(domain, dict), "The 'domain' field should be a dictionary"
        assert login_message['primaryType'] == 'LoginMessage', "The 'primaryType' value is incorrect"
        message = login_message['message']
        assert isinstance(message, dict), "The 'message' field should be a dictionary"
        assert message['message'] == 'I want to log into 100x.finance', "The 'message' value is incorrect"
        types = login_message['types']
        assert isinstance(types, dict), "The 'types' field should be a dictionary"
        assert 'EIP712Domain' in types, "The 'EIP712Domain' key is missing in 'types'"
        assert 'LoginMessage' in types, "The 'LoginMessage' key is missing in 'types'"
        eip712domain = types['EIP712Domain']
        assert isinstance(eip712domain, list), "The 'EIP712Domain' should be a list"
        assert len(eip712domain) == 4, "The 'EIP712Domain' list should contain 4 items"
        loginMessage = types['LoginMessage']
        assert isinstance(loginMessage, list), "The 'LoginMessage' should be a list"
        assert len(loginMessage) == 3, "The 'LoginMessage' list should contain 3 items"

    def test_generate_authenticate_payload(self):
        login_payload = self.auth_instance._generate_authenticate_payload()
        assert 'signature' in login_payload, "The 'signature' field is missing"
        assert 'message' in login_payload, "The 'message' field is missing"
        assert 'account' in login_payload, "The 'account' field is missing"
        assert 'timestamp' in login_payload, "The 'timestamp' field is missing"


# @unittest.skip("Integration tests are slower running, comment to run")
class Class100xPerpetualAuthIntegrationTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.network_address = "0x836eE2b55d173245832995082a8600709c38D099"
        self.private_key = "13e56ca9cceebf1f33065c2c5376ab38570a114bc1b003b60d838f92be9d7930"  # noqa: mock
        self.auth_instance = Class100xPerpetualAuth(network_address=self.network_address, private_key=self.private_key)

    # Integration tests
    def test_authenticate_using_signature(self):
        session_info = self.auth_instance.create_authenticated_session_with_service()

        self.assertIn('name', session_info)
        self.assertEqual(session_info['name'], 'connectedAddress')
        value_pattern = re.compile(r'^v2\.local\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$')
        self.assertRegex(session_info['value'], value_pattern)
