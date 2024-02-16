import unittest

import hummingbot.connector.derivative._100x_perpetual._100x_perpetual_constants as CONSTANTS
from hummingbot.client.config.client_config_map import ClientConfigMap
from hummingbot.client.config.config_helpers import ClientConfigAdapter
from hummingbot.connector.derivative._100x_perpetual._100x_perpetual_derivative import Class100xPerpetualDerivative


class Test100xPerpetualDerivative(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.base_asset = "ETH"
        cls.quote_asset = "USDC"
        cls.trading_pair = f"{cls.base_asset}-{cls.quote_asset}"
        cls.domain = CONSTANTS.TESTNET_DOMAIN

    def setUp(self) -> None:
        super().setUp()

        self.client_config_map = ClientConfigAdapter(ClientConfigMap())

        self.exchange = Class100xPerpetualDerivative(
            client_config_map=self.client_config_map,
            public_key="test_public",
            private_key="test_private",
            trading_pairs=[self.trading_pair],
            domain=self.domain
        )

    def test_100x_perpetual_derivative(self):
        pass
