from decimal import Decimal
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple

import hummingbot.connector.derivative._100x_perpetual._100x_perpetual_constants as CONSTANTS
from hummingbot.connector.constants import s_decimal_NaN
from hummingbot.connector.derivative._100x_perpetual._100x_perpetual_auth import Class100xPerpetualAuth
from hummingbot.connector.perpetual_derivative_py_base import PerpetualDerivativePyBase
from hummingbot.connector.trading_rule import TradingRule
from hummingbot.core.api_throttler.data_types import RateLimit
from hummingbot.core.data_type.common import OrderType, PositionAction, PositionMode, TradeType
from hummingbot.core.data_type.in_flight_order import InFlightOrder, OrderUpdate, TradeUpdate
from hummingbot.core.data_type.order_book_tracker_data_source import OrderBookTrackerDataSource
from hummingbot.core.data_type.trade_fee import TradeFeeBase
from hummingbot.core.data_type.user_stream_tracker_data_source import UserStreamTrackerDataSource
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory

if TYPE_CHECKING:
    from hummingbot.client.config.config_helpers import ClientConfigAdapter


class Class100xPerpetualDerivative(PerpetualDerivativePyBase):
    def __init__(
            self,
            client_config_map: "ClientConfigAdapter",
            public_key: str,
            private_key: str,
            trading_pairs: Optional[List[str]] = None,
            trading_required: bool = True,
            domain: str = CONSTANTS.TESTNET_DOMAIN
    ):
        self._trading_pairs = trading_pairs
        self._trading_required = trading_required
        self._domain = domain
        super().__init__(client_config_map=client_config_map)

    async def _all_trade_updates_for_order(self, order_id: InFlightOrder) -> List[TradeUpdate]:
        trade_updates = []
        return trade_updates

    def _create_order_book_data_source(self) -> OrderBookTrackerDataSource:
        pass

    def _create_user_stream_data_source(self) -> UserStreamTrackerDataSource:
        pass

    def _create_web_assistants_factory(self) -> WebAssistantsFactory:
        pass

    async def _fetch_last_fee_payment(self) -> Tuple[int, Decimal, Decimal]:
        pass

    async def _format_trading_rules(self, exchange_info_dict: Dict[str, Any]) -> List[TradingRule]:
        pass

    def _get_fee(
            self,
            base_currency: str,
            quote_currency: str,
            order_type: OrderType,
            order_side: TradeType,
            position_action: PositionAction,
            amount: Decimal,
            price: Decimal = s_decimal_NaN,
            is_maker: Optional[bool] = None,
    ) -> TradeFeeBase:
        pass

    def _initialize_trading_pair_symbols_from_exchange_info(self) -> Dict[str, str]:
        pass

    def _is_order_not_found_during_cancelation_error(self, cancelation_exception: Exception) -> bool:
        pass

    def _is_order_not_found_during_status_update_error(self, status_update_exception: Exception) -> bool:
        pass

    def _is_request_exception_related_to_time_synchronizer(self, request_exception: Exception) -> bool:
        pass

    async def _place_cancel(self, order_id: str, tracked_order: InFlightOrder):
        pass

    async def _place_order(
            self,
            order_id: str,
            trading_pair: str,
            amount: Decimal,
            trade_type: TradeType,
            order_type: OrderType,
            price: Decimal,
            position_action: PositionAction = PositionAction.NIL,
            **kwargs,
    ) -> Tuple[str, float]:
        pass

    async def _request_order_status(self, tracked_order: InFlightOrder) -> OrderUpdate:
        pass

    async def _set_trading_pair_leverage(self, trading_pair: str, leverage: int) -> Tuple[bool, str]:
        pass

    async def _trading_pair_position_mode_set(self, mode: PositionMode, trading_pair: str) -> Tuple[bool, str]:
        pass

    async def _update_balances(self):
        pass

    async def _update_positions(self):
        pass

    async def _update_trading_fees(self):
        pass

    async def _user_stream_event_listener(self):
        pass

    @property
    def name(self) -> str:
        return CONSTANTS.EXCHANGE_NAME

    @property
    def authenticator(self) -> Class100xPerpetualAuth:
        pass

    @property
    def check_network_request_path(self) -> str:
        return CONSTANTS.PATH_TIME

    @property
    def client_order_id_max_length(self) -> int:
        return CONSTANTS.MAX_ID_LEN

    @property
    def client_order_id_prefix(self) -> str:
        return CONSTANTS.HBOT_BROKER_ID

    @property
    def domain(self) -> str:
        return self._domain

    @property
    def funding_fee_poll_interval(self) -> int:
        return 120

    @property
    def is_cancel_request_in_exchange_synchronous(self) -> bool:
        return False

    @property
    def is_trading_required(self) -> bool:
        return self._trading_required

    @property
    def trading_pairs(self):
        return self._trading_pairs

    @property
    def trading_pairs_request_path(self) -> str:
        return CONSTANTS.EXCHANGE_INFO_URL

    @property
    def trading_rules_request_path(self) -> str:
        return CONSTANTS.EXCHANGE_INFO_URL

    @property
    def rate_limits_rules(self) -> List[RateLimit]:
        return CONSTANTS.RATE_LIMITS

    def get_buy_collateral_token(self, trading_pair: str) -> str:
        pass

    def get_sell_collateral_token(self, trading_pair: str) -> str:
        pass

    def supported_order_types(self) -> List[OrderType]:
        return [OrderType.LIMIT, OrderType.MARKET, OrderType.LIMIT_MAKER]

    def supported_position_modes(self):
        return [PositionMode.ONEWAY]
