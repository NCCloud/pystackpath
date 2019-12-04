import json
from pystackpath.util import BaseObject, pagination_query, PageInfo


class Rules(BaseObject):
    def index(self, first="", after="", filter="", sort_by=""):
        """
        Retrieve the waf rules on a site
        :return: a list of rules on a site
        """
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get(f"{self._base_api}/rules",
                                    params=pagination)
        items = [self.loaddict(item) for item in response.json()["rules"]]
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def get(self, rule_id):
        response = self._client.get(f"{self._base_api}/rules/{rule_id}")
        return self.loaddict(response.json()["rule"])

    def create(self, **payload):
        """
        Add a waf rule to a site
        :param payload: dict according to https://stackpath.dev/reference/rules#createrule
        :return: dict with created rule
        """
        response = self._client.post(f"{self._base_api}/rules", json=payload)
        return self.loaddict(response.json()["rule"])

    def update(self, **payload):
        """
        Update a WAF rule
        :param payload: dict according to https://stackpath.dev/reference/rules#updaterule
        :return: dict with new rule
        """
        response = self._client.patch(f"{self._base_api}/rules/{self.id}", data=json.dumps(payload))
        return self.loaddict(response.json()["rule"])

    def delete(self):
        """
        Remove a eaf from a site
        :return: waf rule configured on a site
        """
        response = self._client.delete(f"{self._base_api}/rules/{self.id}")
        return self

    def bulk_delete(self, ruleIds: list):
        """
        Delete multiple WAF rules
        :param ruleIds: The IDs of the rules to delete.
        """
        response = self._client.post(f"{self._base_api}/rules/bulk_delete", data=json.dumps(dict(ruleIds=ruleIds)))

    def enable(self):
        """
        Enable a WAF rule
        """
        response = self._client.post(f"{self._base_api}/rules/{self.id}/enable")

    def disable(self):
        """
        Disable a WAF rule
        """
        response = self._client.post(f"{self._base_api}/rules/{self.id}/disable")
