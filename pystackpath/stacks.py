from .util import BaseObject, PageInfo, pagination_query
from .cdnsites import CdnSites
from .metrics import Metrics
from .certificates import Certificates


class Stacks(BaseObject):
    def index(self, first="", after="", filter="", sort_by=""):
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get("/stack/v1/stacks", params=pagination)
        response.raise_for_status()
        items = []
        for item in response.json()["results"]:
            items.append(self.loaddict(item))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def get(self, stack_id):
        response = self._client.get("/stack/v1/stacks/{}".format(stack_id))
        response.raise_for_status()
        return self.loaddict(response.json())

    def create(self, accountid, name):
        response = self._client.post("/stack/v1/stacks",
                                     json={"accountId": accountid, "name": str(name)})
        response.raise_for_status()
        return self.loaddict(response.json()["stack"])

    def add_subscriptions(self, subscriptions: list):
        response = self._client.post(
            "/billing/v1/stacks/{}/subscriptions".format(self.id),
            json={
                "productIds": subscriptions
            }
        )
        response.raise_for_status()
        return self

    def cancel(self, reason_slug, reason_text=""):
        reason_slugs = [
            "not-reliable",
            "no-desired-location",
            "missing-feature",
            "taking-too-long",
            "setup-difficult",
            "price",
            "other"
        ]
        if reason_slug not in reason_slugs:
            raise ValueError('Invalid reason slug')

        response = self._client.post(
            "/billing/v1/stacks/{}/cancel".format(self.id),
            json={
                "reasonSlug": reason_slug,
                "reasonText": reason_text
            }
        )
        response.raise_for_status()
        return self

    def purge(self, items: list):
        data = {
            "items": items
        }

        response = self._client.post("/cdn/v1/stacks/{}/purge".format(self.id), json=data)
        response.raise_for_status()

        return self.loaddict(response.json())

    def purge_status(self, purge_id):

        response = self._client.get(f"/cdn/v1/stacks/{self.id}/purge/{purge_id}")
        response.raise_for_status()

        return self.loaddict(response.json())

    def cdnsites(self):
        return CdnSites(self._client, self.id)

    def metrics(self):
        return Metrics(self._client, self.id)

    def certificates(self):
        return Certificates(self._client, self.id)
