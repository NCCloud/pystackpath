from pystackpath.util import BaseObject, PageInfo


class Origins(BaseObject):
    def index(self):
        response = self._client.get(f"{self._base_api}")
        response.raise_for_status()

        items = list(map(lambda x: self.loaddict(x), response.json()["results"]))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def create(self, **payload):
        """
        Create a new CDN origin
        :param payload: dict according to https://stackpath.dev/reference/configuration#connectscopetoorigin
        :return: dict with requested origin
        String	id         An origin's unique identifier.
        String	path       An origin's path.
        String	hostname   An origin's hostname or IP address.
        Integer	port       The HTTP port to connect to the origin.
        Integer	securePort The HTTPS port to connect to the origin.
        Boolean	dedicated  Whether or not an origin is dedicated to a CDN site.
        """
        response = self._client.post(f"{self._base_api}", json=payload)
        response.raise_for_status()
        return self.loaddict(response.json()["scopeOrigin"])

    def delete(self):
        """
        Delete the current origin.

        :return:
        """
        response = self._client.delete(f"{self._base_api}")
        response.raise_for_status()
        return self
