from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit

EXCHANGE_NAME = "100x_perpetual"

DOMAIN = EXCHANGE_NAME
TESTNET_DOMAIN = "100x_perpetual_testnet"

PERPETUAL_BASE_URL = "https://api.100x.finance/"
TESTNET_BASE_URL = "https://api.ciaobella.dev/"

PERPETUAL_WS_URL = "wss://api.100x.finance/"
TESTNET_WS_URL = "wss://api.ciaobella.dev/"

# Public API v1 Endpoints
PRODUCTS_URL = "v1/products"
LOGIN = "v1/session/login"
PING_URl = "v1/time"

MAX_REQUEST = 1_200
ALL_ENDPOINTS_LIMIT = "All"

RATE_LIMITS = [
    RateLimit(limit_id=ALL_ENDPOINTS_LIMIT, limit=MAX_REQUEST, time_interval=60),

    # Weight limits for individual endpoints
    RateLimit(limit_id=PRODUCTS_URL, limit=MAX_REQUEST, time_interval=60,
              linked_limits=[LinkedLimitWeightPair(limit_id=ALL_ENDPOINTS_LIMIT)]),
    RateLimit(limit_id=PING_URl, limit=MAX_REQUEST, time_interval=60,
              linked_limits=[LinkedLimitWeightPair(limit_id=ALL_ENDPOINTS_LIMIT)])
]

LOGIN_MESSAGE = "I want to log into 100x.finance"
