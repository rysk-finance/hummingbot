import time

import eth_account
import requests
from eip712_structs import Address, EIP712Struct, String, Uint, make_domain
from eth_account.messages import encode_structured_data

from hummingbot.connector.derivative._100x_perpetual._100x_perpetual_constants import LOGIN_MESSAGE
from hummingbot.connector.derivative._100x_perpetual._100x_perpetual_web_utils import public_rest_url
from hummingbot.core.web_assistant.auth import AuthBase


class LoginMessage(EIP712Struct):
    account = Address()
    message = String()
    timestamp = Uint(64)


class Class100xPerpetualAuth(AuthBase):

    def __init__(self, public_key: str, private_key: str):
        self.domain = make_domain(name="Ciao", version="0.0.0", chainId=168587773, verifyingContract="0xe5fCf48E0E06252b0b237b9237Ce6B4Ec2145aB0")
        self.private_key: str = private_key
        self.public_key: str = public_key
        self.wallet = eth_account.Account.from_key(private_key)
        self.session_cookie = {}

    def _current_timestamp(self):
        timestamp_ms = int(time.time() * 1000)
        return timestamp_ms

    def _generate_eip_712_login_message(self):
        login_message = LoginMessage(account=self.public_key,
                                     message=LOGIN_MESSAGE,
                                     timestamp=self._current_timestamp()
                                     )
        return login_message.to_message(self.domain)

    def _sign_eip_712_login_message(self, login_data: dict):
        signable_message = encode_structured_data(login_data)
        signed = self.wallet.sign_message(signable_message)
        return signed

    def _extract_message_append_signature(self, login_message, signed):
        signature = signed.signature
        message = login_message['message']
        message['signature'] = signature.hex()
        return message

    def _generate_authenticate_payload(self):
        login_message = self._generate_eip_712_login_message()
        signed = self._sign_eip_712_login_message(login_message)
        message = self._extract_message_append_signature(login_message, signed)
        return message

    def create_authenticated_session_with_service(self):
        login_payload = self._generate_authenticate_payload()
        url = public_rest_url(path_url="v1/session/login", domain="testnet")
        headers = {
            "Content-type": "application/json",
        }
        response = requests.post(url, headers=headers, json=login_payload)

        if response.status_code == 200:
            response = response.json()
            self.session_cookie = response
        return response

    def rest_authenticate(self):
        # Implementation of REST authentication logic here
        pass

    def ws_authenticate(self):
        # Implementation of WebSocket authentication logic here
        pass
