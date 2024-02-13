import hummingbot.connector.derivative._100x_perpetual._100x_perpetual_constants as CONSTANTS
from hummingbot.core.web_assistant.connections.data_types import RESTMethod, RESTRequest
from hummingbot.core.web_assistant.rest_pre_processors import RESTPreProcessorBase


class Class100xPerpetualRESTPreProcessor(RESTPreProcessorBase):

    async def pre_process(self, request: RESTRequest) -> RESTRequest:
        if request.headers is None:
            request.headers = {}
        request.headers["Content-Type"] = (
            "application/json" if request.method == RESTMethod.POST else "application/x-www-form-urlencoded"
        )
        return request

    def public_rest_url(self, path_url: str, domain: str = "100x_perpetual"):
        base_url = CONSTANTS.PERPETUAL_BASE_URL if domain == "100x_perpetual" else CONSTANTS.TESTNET_BASE_URL
        return base_url + path_url
