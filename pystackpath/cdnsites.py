from .util import BaseObject, PageInfo, pagination_query


class CdnSites(BaseObject):
    def index(self, first="", after="", filter="", sort_by=""):
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get("/cdn/v1/stacks/{}/sites".format(self._parent_id), params=pagination)
        response.raise_for_status()
        items = []
        for item in response.json()["results"]:
            items.append(self.loaddict(item))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def get(self, site_id):
        response = self._client.get("/cdn/v1/stacks/{}/sites/{}".format(self._parent_id, site_id))
        response.raise_for_status()
        return self.loaddict(response.json()["site"])

    def create(self, domain, origin_hostname):
        response = self._client.post(
            "/cdn/v1/stacks/{}/sites".format(self._parent_id),
            json={
                "domain": domain,
                "origin": {
                    "hostname": origin_hostname
                }
            }
        )
        response.raise_for_status()
        return self.loaddict(response.json()["site"])

    def delete(self):
        response = self._client.delete("/cdn/v1/stacks/{}/sites/{}".format(self._parent_id, self.id))
        response.raise_for_status()
        return self