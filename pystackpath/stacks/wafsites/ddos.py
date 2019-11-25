import json
from pystackpath.util import BaseObject


class Ddos(BaseObject):
    def get(self):
        response = self._client.get(f"{self._base_api}/ddos")
        response.raise_for_status()
        return self.loaddict(response.json()["ddosSettings"])

    def update(self, **payload):
        """
        Update a WAF ddos setting
        :param payload: dict according to https://stackpath.dev/reference/waf-features#updateddossettings
        :return: dict with new rule
        """
        response = self._client.patch(f"{self._base_api}/ddos", data=json.dumps(payload))
        response.raise_for_status()
        return self.loaddict(response.json()["ddosSettings"])
