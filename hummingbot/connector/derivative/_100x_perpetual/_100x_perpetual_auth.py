import time

import eth_account
from eip712_structs import Address, EIP712Struct, String, Uint, make_domain
from eth_account.messages import encode_structured_data

from hummingbot.connector.derivative._100x_perpetual._100x_perpetual_constants import LOGIN_MESSAGE
from hummingbot.core.web_assistant.auth import AuthBase


class LoginMessage(EIP712Struct):
    account = Address()
    message = String()
    timestamp = Uint(64)


class Class100xPerpetualAuth(AuthBase):

    def __init__(self, network_address: str, private_key: str):
        self.private_key: str = private_key
        self.network_address: str = network_address
        self.wallet = eth_account.Account.from_key(private_key)
        self.domain = make_domain(name="ciao", version="0.0.0", chainId=1337, verifyingContract="0x0000000000000000000000000000000000000000")

    def _current_timestamp(self):
        timestamp_ms = int(time.time() * 1000)
        return timestamp_ms

    def _generate_eip_712_login_message(self):
        login_message = LoginMessage(account=self.network_address,
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

    def rest_authenticate(self):
        # Implementation of REST authentication logic here
        pass

    def ws_authenticate(self):
        # Implementation of WebSocket authentication logic here
        pass
