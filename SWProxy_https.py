import json
import time
from pathlib import Path
from random import randint, shuffle

from mitmproxy import ctx, http

from SWPlugin import SWPlugin
from SWParser.smon_decryptor import decrypt_request, decrypt_response


class SW_Handler():

    def __init__(self, config: str = "swproxy.config"):
        self.config = config
        self.sw_request = None
        SWPlugin.set_config_name(config=config)

    def request(self, flow: http.HTTPFlow) -> None:
        if "api/gateway" in flow.request.pretty_url:
            self.sw_request = flow.request
        else:
            self.sw_request = None

    def response(self, flow: http.HTTPFlow) -> None:
        if self.sw_request is None:
            return

        try:
            req_plain, req_json = self._parse_request(flow)
            resp_plain, resp_json = self._parse_response(flow)

            if 'command' not in resp_json:
                self.sw_request = None
                return
            try:
                SWPlugin.call_plugins('process_request', (req_json, resp_json))
            except Exception as e:
                ctx.log.error(f"Exception while executing plugin : {e}")
        except Exception as e:
            ctx.log.error(f"Unknown exception {e}")

    def _parse_request(self, flow):
        plain = decrypt_request(flow.request.get_text(), 2 if '_c2.php' in flow.request.pretty_url else 1)
        return plain, json.loads(plain)

    def _parse_response(self, flow):
        plain = decrypt_response(flow.request.get_text(), 2 if '_c2.php' in flow.request.pretty_url else 1)
        return plain, json.loads(plain)


addons = [SW_Handler()]
