import json
from pystackpath.util import BaseObject


class Monitoring(BaseObject):
    def create(self):
        """
        Place a WAF site into monitoring mode
        :return:
        """
        response = self._client.post(f"{self._base_api}/monitoring")
        return self

    def delete(self):
        """
        Remove a WAF site from monitoring mode
        :return:
        """
        response = self._client.delete(f"{self._base_api}/monitoring")
        return self