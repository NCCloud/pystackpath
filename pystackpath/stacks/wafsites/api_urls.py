import json
from pystackpath.util import BaseObject


class ApiUrls(BaseObject):
    def update(self, **payload):
        """
        Update API site's URLs
        :param payload: dict according to https://stackpath.dev/reference/waf-features#updatesiteapiurls
        :return: A list of API URLs
        """
        response = self._client.put(f"{self._base_api}/api_urls", data=json.dumps(payload))
        return response.json()["apiUrls"]
