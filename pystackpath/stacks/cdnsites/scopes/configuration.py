from pystackpath.util import BaseObject, pagination_query, PageInfo


class Configuration(BaseObject):
    def get(self):
        """
        Retrieve a CDN site's scope configuration
        :return: site's scope configuration
        """
        response = self._client.get(f"{self._base_api}/configuration")
        response.raise_for_status()
        return self.loaddict(response.json()["configuration"])

    def update(self, **payload):
        """
        Update a CDN site's scope configuration
        :param payload: dict according to https://stackpath.dev/reference/configuration#updatescopeconfiguration
        :return: dict with new configuration
        """
        response = self._client.post(f"{self._base_api}/configuration", json=payload)
        response.raise_for_status()
        return self.loaddict(response.json()["configuration"])
