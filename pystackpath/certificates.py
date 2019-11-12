from .util import BaseObject, PageInfo, pagination_query

class Certificates(BaseObject):
        def index(self, first="", after="", filter="", sort_by=""):
            pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
            response = self._client.get(f"/cdn/v1/stacks/{self._parent_id}/certificates", params=pagination)
            response.raise_for_status()
            items = []
            for item in response.json()["results"]:
                items.append(self.loaddict(item))
            pageinfo = PageInfo(**response.json()["pageInfo"])

            return {"results": items, "pageinfo": pageinfo}


        def get(self, certificate_id):
            ##https://gateway.stackpath.com/cdn/v1/stacks/{stack_id}/certificates/{certificate_id}
            response = self._client.get(f"/cdn/v1/stacks/{self._parent_id}/certificates/{certificate_id}")
            response.raise_for_status()

            return response
