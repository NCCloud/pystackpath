from pystackpath.util import BaseObject
from pystackpath.stacks.wafsites.policy_groups.policies import Policies


class PolicyGroups(BaseObject):
    def index(self):
        """
        Retrieve all WAF policy groups
        :return: a list of policy groups on a site
        """
        response = self._client.get(f"{self._base_api}/policy_groups")
        items = [self.loaddict(item) for item in response.json()["policyGroups"]]

        return items

    def get(self, policy_group_id):
        """
        Retrieve an individual WAF policy group
        :param policy_group_id: The ID of the WAF policy group to retrieve
        """
        response = self._client.get(f"{self._base_api}/policy_groups/{policy_group_id}")
        return self.loaddict(response.json()["policyGroup"])

    def enable(self):
        """
        Enable all policies in a WAF policy group
        """
        response = self._client.post(f"{self._base_api}/policy_groups/{self.id}/enable")

    def disable(self):
        """
        Disable all policies in a WAF policy group
        """
        response = self._client.post(f"{self._base_api}/policy_groups/{self.id}/disable")

    def policies(self):
        return Policies(self._client, f"{self._base_api}/policy_groups/{self.id}")
