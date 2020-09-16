from pystackpath.util import BaseObject, PageInfo, pagination_query


class Records(BaseObject):
    def index(self, first="", after="", filter="", sort_by=""):
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get(f"{self._base_api}/records", params=pagination)

        items = list(map(lambda x: self.loaddict(x), response.json()["records"]))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"records": items, "pageinfo": pageinfo}

    def get(self, record_id: str):
        response = self._client.get(f"{self._base_api}/records/{record_id}")
        return self.loaddict(response.json()["record"])

    def add(self, **payload):
        response = self._client.post(f"{self._base_api}/records", json=payload)
        return self.loaddict(response.json()["record"])

    def delete(self):
        response = self._client.delete(f"{self._base_api}/records/{self.id}")
        return self

    def update(self, **payload):
        response = self._client.patch(f"{self._base_api}/records/{self.id}", json=payload)
        return self.loaddict(response.json()["record"])

    def replace(self, **payload):
        response = self._client.put(f"{self._base_api}/records/{self.id}", json=payload)
        return self.loaddict(response.json()["record"])
