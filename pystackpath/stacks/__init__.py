from pystackpath.util import BaseObject, PageInfo, pagination_query
from pystackpath.stacks.cdnsites import CdnSites
from pystackpath.stacks.deliverysites import DeliverySites
from pystackpath.stacks.wafsites import WafSites
from pystackpath.stacks.metrics import Metrics
from pystackpath.stacks.certificates import Certificates


class Stacks(BaseObject):
    def index(self, first="", after="", filter="", sort_by=""):
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get("/stack/v1/stacks", params=pagination)
        items = []
        for item in response.json()["results"]:
            items.append(self.loaddict(item))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def get(self, stack_id):
        response = self._client.get(f"/stack/v1/stacks/{stack_id}")
        return self.loaddict(response.json())

    def create(self, accountid, name):
        response = self._client.post("/stack/v1/stacks",
                                     json={"accountId": accountid, "name": str(name)})
        return self.loaddict(response.json()["stack"])

    def add_subscriptions(self, subscriptions: list):
        response = self._client.post(
            f"/billing/v1/stacks/{self.id}/subscriptions",
            json={
                "productIds": subscriptions
            }
        )
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
            f"/billing/v1/stacks/{self.id}/cancel",
            json={
                "reasonSlug": reason_slug,
                "reasonText": reason_text
            }
        )
        return self

    def purge(self, items: list) -> str:
        """
        Purge cached content for all CDN sites on a stack
        :param items: The items to purge from the CDN.
        :return: The purge request's ID.
        """
        data = {
            "items": items
        }

        response = self._client.post(f"/cdn/v1/stacks/{self.id}/purge", json=data)

        return response.json()["id"]

    def purge_status(self, purge_id) -> float:
        """
        Retrieve a purge request's status
        :param purge_id: The ID of the purge request to check the status of
        :return: The purge request's progress, ranging from 0.0 to 1.0.
        """
        response = self._client.get(f"/cdn/v1/stacks/{self.id}/purge/{purge_id}")

        return response.json()["progress"]

    def deliverysites(self):
        return DeliverySites(self._client, f"/delivery/v1/stacks/{self.id}")

    def cdnsites(self):
        return CdnSites(self._client, f"/cdn/v1/stacks/{self.id}")

    def wafsites(self):
        return WafSites(self._client, f"/waf/v1/stacks/{self.id}")

    def metrics(self):
        return Metrics(self._client, f"/cdn/v1/stacks/{self.id}")

    def certificates(self):
        return Certificates(self._client, f"/cdn/v1/stacks/{self.id}")
