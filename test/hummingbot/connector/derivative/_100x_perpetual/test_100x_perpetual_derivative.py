import json
from decimal import Decimal
from typing import Any, Callable, List, Optional
from unittest.mock import AsyncMock

from aioresponses import aioresponses

import hummingbot.connector.derivative._100x_perpetual._100x_perpetual_constants as CONSTANTS
import hummingbot.connector.derivative._100x_perpetual._100x_perpetual_web_utils as web_utils
from hummingbot.client.config.client_config_map import ClientConfigMap
from hummingbot.client.config.config_helpers import ClientConfigAdapter
from hummingbot.connector.derivative._100x_perpetual._100x_perpetual_derivative import Class100xPerpetualDerivative
from hummingbot.connector.test_support.perpetual_derivative_test import AbstractPerpetualDerivativeTests
from hummingbot.connector.trading_rule import TradingRule
from hummingbot.core.data_type.common import OrderType, PositionMode
from hummingbot.core.data_type.in_flight_order import InFlightOrder
from hummingbot.core.data_type.trade_fee import TradeFeeBase
from hummingbot.core.network_iterator import NetworkStatus


class Test100xPerpetualDerivative(AbstractPerpetualDerivativeTests.PerpetualDerivativeTests):

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

    @property
    def all_symbols_request_mock_response(self):
        mock_response = [
            {
                "id": 1002,
                "type": "PERP",
                "symbol": "ethperp",
                "active": True,
                "baseAsset": "ETH",
                "quoteAsset": "USDC",
                "minQuantity": "1000000000000000",
                "maxQuantity": "1000000000000000000000000",
                "increment": "100000000000000",
                "takerFee": 200000000000000,
                "makerFee": 50000000000000,
                "isMakerRebate": True,
                "initialLongWeight": 95000000000000000,
                "initialShortWeight": 1050000000000000000,
                "maintenanceLongWeight": 97000000000000000,
                "maintenanceShortWeight": 1030000000000000000
            }
        ]
        return mock_response

    @property
    def all_symbols_including_invalid_pair_mock_response(self):
        mock_response = self.all_symbols_request_mock_response
        return "INVALID-PAIR", mock_response

    @property
    def all_symbols_url(self):
        url = web_utils.public_rest_url(CONSTANTS.PRODUCTS_URL, domain=self.domain)
        return url

    def balance_event_websocket_update(self):
        pass

    def balance_request_mock_response_for_base_and_quote(self) -> Any:
        pass

    def balance_request_mock_response_only_base(self) -> Any:
        pass

    def balance_url(self) -> str:
        pass

    @aioresponses()
    def test_all_trading_pairs(self, mock_api):
        self.exchange._set_trading_pair_symbol_map(None)

        self.configure_all_symbols_response(mock_api=mock_api)

        all_trading_pairs = self.async_run_with_timeout(coroutine=self.exchange.all_trading_pairs())

        # expected_valid_trading_pairs = self._expected_valid_trading_pairs()

        self.assertEqual(1, len(all_trading_pairs))
        self.assertIn(self.trading_pair, all_trading_pairs)

    def configure_all_symbols_response(
            self,
            mock_api: aioresponses,
            callback: Optional[Callable] = lambda *args, **kwargs: None,
    ) -> List[str]:

        url = self.all_symbols_url
        response = self.all_symbols_request_mock_response
        mock_api.get(url, body=json.dumps(response), callback=callback)
        return [url]

    def configure_canceled_order_status_response(self):
        pass

    def configure_completely_filled_order_status_response(self):
        pass

    def configure_erroneous_cancelation_response(self):
        pass

    def configure_erroneous_http_fill_trade_response(self):
        pass

    def configure_failed_set_leverage(self):
        pass

    def configure_failed_set_position_mode(self, position_mode: PositionMode, mock_api: AsyncMock, callback: Optional[Callable] = None):
        pass

    def configure_full_fill_trade_response(self):
        pass

    def configure_http_error_order_status_response(self):
        pass

    def configure_one_successful_one_erroneous_cancel_all_response(self):
        pass

    def configure_open_order_status_response(self):
        pass

    def configure_order_not_found_error_cancelation_response(self):
        pass

    def configure_order_not_found_error_order_status_response(self):
        pass

    def configure_partial_fill_trade_response(self):
        pass

    def configure_partially_filled_order_status_response(self):
        pass

    def configure_successful_cancelation_response(self):
        pass

    def configure_successful_set_leverage(self, leverage: int, mock_api: AsyncMock, callback: Optional[Callable] = None):
        pass

    def configure_successful_set_position_mode(self, position_mode: PositionMode, mock_api: AsyncMock, callback: Optional[Callable] = None):
        pass

    def create_exchange_instance(self):
        client_config_map = ClientConfigAdapter(ClientConfigMap())
        exchange = Class100xPerpetualDerivative(
            client_config_map=client_config_map,
            public_key="test_public",
            private_key="test_private",
            trading_pairs=[self.trading_pair],
            domain=self.domain
        )
        return exchange

    def empty_funding_payment_mock_response(self):
        pass

    def exchange_symbol_for_tokens(self, base_token: str, quote_token: str) -> str:
        pass

    def expected_exchange_order_id(self) -> str:
        pass

    def expected_fill_fee(self) -> TradeFeeBase:
        pass

    def expected_fill_trade_id(self) -> str:
        pass

    def expected_latest_price(self) -> Decimal:
        pass

    def expected_logged_error_for_erroneous_trading_rule(self):
        pass

    def expected_partial_fill_amount(self) -> Decimal:
        pass

    def expected_partial_fill_price(self) -> Decimal:
        pass

    def expected_supported_order_types(self) -> List[OrderType]:
        pass

    def expected_supported_position_modes(self) -> List[PositionMode]:
        pass

    def expected_trading_rule(self):
        pass

    def funding_info_event_for_websocket_update(self):
        pass

    def funding_info_mock_response(self):
        pass

    def funding_info_url(self):
        pass

    def funding_payment_mock_response(self):
        pass

    def funding_payment_url(self):
        pass

    def is_order_fill_http_update_executed_during_websocket_order_event_processing(self) -> bool:
        pass

    def is_order_fill_http_update_included_in_status_update(self) -> bool:
        pass

    def latest_prices_request_mock_response(self):
        pass

    def latest_prices_url(self):
        pass

    def network_status_request_successful_mock_response(self):
        mock_response = {
            "serverTime": 1708616915512
        }
        return mock_response

    @property
    def network_status_url(self):
        return web_utils.public_rest_url(CONSTANTS.PING_URl, domain=self.domain)

    def order_creation_request_successful_mock_response(self):
        pass

    def order_creation_url(self):
        pass

    def order_event_for_canceled_order_websocket_update(self):
        pass

    def order_event_for_full_fill_websocket_update(self):
        pass

    def order_event_for_new_order_websocket_update(self):
        pass

    def position_event_for_full_fill_websocket_update(self, unrealized_pnl: float):
        pass

    def trade_event_for_full_fill_websocket_update(self):
        pass

    def trading_rules_request_erroneous_mock_response(self):
        pass

    def trading_rules_request_mock_response(self):
        pass

    def trading_rules_url(self):
        pass

    def validate_auth_credentials_present(self, request_call: AsyncMock):
        pass

    def validate_order_cancelation_request(self, order: InFlightOrder, request_call: AsyncMock):
        pass

    def validate_order_creation_request(self, order: InFlightOrder, request_call: AsyncMock):
        pass

    def validate_order_status_request(self, order: InFlightOrder, request_call: AsyncMock):
        pass

    def validate_trades_request(self, order: InFlightOrder, request_call: AsyncMock):
        pass

    @property
    def balance_request_mock_response_only_quote(self):
        mock_response = {
            "account": {
                "starkKey": "180913017c740260fea4b2c62828a4008ca8b0d6e4",
                "positionId": "1812",
                "equity": "10000",
                "freeCollateral": "10000",
                "quoteBalance": "10000",
                "pendingDeposits": "0",
                "pendingWithdrawals": "0",
                "createdAt": "2021-04-09T21:08:34.984Z",
                "openPositions": {
                    self.trading_pair: {
                        "market": self.trading_pair,
                        "status": "OPEN",
                        "side": "LONG",
                        "size": "1000",
                        "maxSize": "1050",
                        "entryPrice": "100",
                        "exitPrice": None,
                        "unrealizedPnl": "50",
                        "realizedPnl": "100",
                        "createdAt": "2021-01-04T23:44:59.690Z",
                        "closedAt": None,
                        "netFunding": "500",
                        "sumOpen": "1050",
                        "sumClose": "50",
                    }
                },
                "accountNumber": "5",
                "id": "id",
            }
        }
        return mock_response

    def _simulate_trading_rules_initialized(self):
        self.exchange._trading_rules = {
            self.trading_pair: TradingRule(
                trading_pair=self.trading_pair,
                min_order_size=Decimal(str(0.01)),
                min_price_increment=Decimal(str(0.0001)),
                min_base_amount_increment=Decimal(str(0.000001)),
            )
        }

    def test_get_buy_and_sell_collateral_tokens(self):
        self._simulate_trading_rules_initialized()

        buy_collateral_token = self.exchange.get_buy_collateral_token(self.trading_pair)
        sell_collateral_token = self.exchange.get_sell_collateral_token(self.trading_pair)

        self.assertEqual(buy_collateral_token, self.quote_asset)
        self.assertEqual(sell_collateral_token, self.quote_asset)

    @aioresponses()
    def test_update_balances(self, mock_api):
        response = self.balance_request_mock_response_only_quote

        self._configure_balance_response(response=response, mock_api=mock_api)
        self.async_run_with_timeout(self.exchange._update_balances())

        available_balances = self.exchange.available_balances
        total_balances = self.exchange.get_all_balances()

        self.assertNotIn(self.base_asset, available_balances)
        self.assertNotIn(self.base_asset, total_balances)
        self.assertEqual(Decimal("10000"), available_balances["USD"])
        self.assertEqual(Decimal("10000"), total_balances["USD"])

    @aioresponses()
    def test_check_network_success(self, mock_api):
        url = self.network_status_url
        response = self.network_status_request_successful_mock_response
        mock_api.get(url, body=response)

        network_status = self.async_run_with_timeout(coroutine=self.exchange.check_network())

        self.assertEqual(NetworkStatus.CONNECTED, network_status)
