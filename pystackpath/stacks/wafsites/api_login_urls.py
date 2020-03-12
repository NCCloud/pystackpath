import json
from pystackpath.util import BaseObject


class ApiLoginUrls(BaseObject):
    def update(self, **payload):
        """
        Update API site's login URLs
        :param payload: dict according to https://stackpath.dev/reference/waf-features#updatesiteapiloginurls
        :return: A list of API login URLs
        """
        response = self._client.put(f"{self._base_api}/api_login_urls", data=json.dumps(payload))
        return response.json()["apiLoginUrls"]
