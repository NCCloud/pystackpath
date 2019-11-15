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
            response = self._client.get(f"/cdn/v1/stacks/{self._parent_id}/certificates/{certificate_id}")
            response.raise_for_status()

            return self.loaddict(response.json()["certificate"])


        def add(self, certificate_string, key_string, ca_bundle_string = None):

            data = {
                "certificate" : certificate_string,
                "key" : key_string,
                "caBundle" : ca_bundle_string
            }

            response = self._client.post(f"/cdn/v1/stacks/{self._parent_id}/certificates", json = data)
            response.raise_for_status()

            return self.loaddict(response.json()["certificate"])

        def delete(self, certificate_id):

            response = self._client.delete(f"/cdn/v1/stacks/{self._parent_id}/certificates/{certificate_id}" )
            response.raise_for_status()

            return self

        def update(self, certificate_id, certificate_string = None, key_string = None, ca_bundle_string = None):

            data = {
                "certificate" : certificate_string,
                "key" : key_string,
                "caBundle" : ca_bundle_string
            }

            response = self._client.put(f"/cdn/v1/stacks/{self._parent_id}/certificates/{certificate_id}",
                json = data )
            response.raise_for_status()

            return self.loaddict(response.json()["certificate"])

        def renew(self, certificate_id):

            response = self._client.post(f"/cdn/v1/stacks/{self._parent_id}/certificates/{certificate_id}/renew")
            response.raise_for_status()

            return response
