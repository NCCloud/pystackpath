from pystackpath.stacks.cdnsites.scopes.configuration import Configuration
from pystackpath.stacks.cdnsites.scopes.origins import Origins
from pystackpath.util import BaseObject, pagination_query, PageInfo


class Scopes(BaseObject):
    def index(self, first="", after="", filter="", sort_by="", disable_transparent_mode=None):
        """
        Retrieve a CDN site's scopes
        :return: a list of site scopes
        """
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        params = {
            "disable_transparent_mode": disable_transparent_mode
        }
        response = self._client.get(f"{self._base_api}/scopes",
                                    params={**pagination, **params})
        response.raise_for_status()
        items = [self.loaddict(item) for item in response.json()["results"]]
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def create(self, **payload):
        """
        Create a new CDN site scope
        :param payload: dict according to https://stackpath.dev/reference/configuration#createscope
        :return: dict with created site
        String	id         A CDN site scope's unique identifier.
        String	platform   A CDN site scope's platform.
                           Scope platforms are used internally by StackPath for metrics collection and billing purposes.
                           Typically, most site scope platforms have the value "CDS"
        String	path       The HTTP request path that is handled by a scope.
        """
        response = self._client.post(f"{self._base_api}/scopes", json=payload)
        response.raise_for_status()
        return self.loaddict(response.json()["scope"])

    def delete(self):
        """
        Delete a CDN site scope
        :return: delivery domains configured on a site
        """
        response = self._client.delete(f"{self._base_api}/scopes/{self.id}")
        response.raise_for_status()
        return self

    def configuration(self):
        return Configuration(self._client, f"{self._base_api}/scopes/{self.id}")

    def origins(self):
        """
        Handling Origin resources attached to the current scope.

        :return:
        """
        return Origins(self._client, f"{self._base_api}/scopes/{self.id}/origins")
