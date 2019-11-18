from pystackpath.util import BaseObject, PageInfo, pagination_query


class Certificates(BaseObject):
    def index(self, first="", after="", filter="", sort_by=""):
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get(f"{self._base_api}/certificates", params=pagination)
        response.raise_for_status()

        items = list(map(lambda x: self.loaddict(x), response.json()["results"]))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def get(self, certificate_id: str):
        response = self._client.get(f"{self._base_api}/certificates/{certificate_id}")
        response.raise_for_status()

        return self.loaddict(response.json()["certificate"])

    def add(self, certificate_string: str, key_string: str, ca_bundle_string: str = None):
        data = {
            "certificate" : certificate_string,
            "key" : key_string,
            "caBundle" : ca_bundle_string
        }

        response = self._client.post(f"{self._base_api}/certificates", json=data)
        response.raise_for_status()

        return self.loaddict(response.json()["certificate"])

    def delete(self):
        response = self._client.delete(f"{self._base_api}/certificates/{self.id}")
        response.raise_for_status()

        return self

    def update(self, certificate_string = None, key_string = None, ca_bundle_string: str = None):
        data = {
            "certificate" : certificate_string,
            "key" : key_string,
            "caBundle" : ca_bundle_string
        }

        response = self._client.put(f"{self._base_api}/certificates/{self.id}", json=data)
        response.raise_for_status()

        return self.loaddict(response.json()["certificate"])

    def renew(self):
        response = self._client.post(f"{self._base_api}/certificates/{self.id}/renew")
        response.raise_for_status()

        return self
