from pystackpath.util import BaseObject, pagination_query, PageInfo


class DeliveryDomains(BaseObject):
    def index(self, first="", after="", filter="", sort_by=""):
        """
        Retrieve the delivery domains configured on a site
        :return: a list of domains configures on a site
        """
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get(f"{self._base_api}/delivery_domains",
                                    params=pagination)
        response.raise_for_status()
        items = [self.loaddict(item) for item in response.json()["results"]]
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def create(self, **payload):
        """
        Add a delivery domain to a site
        :param payload: dict according to https://stackpath.dev/reference/delivery-domains#createsitedeliverydomain
        :return: dict with created site
        String	domain     An individual delivery domain.
        """
        response = self._client.post(f"{self._base_api}/delivery_domains", json=payload)
        response.raise_for_status()
        return self.loaddict(response.json()["domain"])

    def delete(self):
        """
        Remove a delivery domain from a site
        :return: delivery domains configured on a site
        """
        response = self._client.delete(f"{self._base_api}/delivery_domains/{self.domain}")
        response.raise_for_status()
        return self
