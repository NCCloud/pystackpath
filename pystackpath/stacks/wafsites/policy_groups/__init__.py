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

    def update(self, policy_groups):
        """
        Update all the policies in the given policy_groups

        :param policy_groups: List of policy groups

        Example:
            [
                {
                    "id": "d694f10e-7faf-4517-bc5b-265e95c04442",
                    "policies": [{ "enabled": false, "id": "S8758188" }]
                }
            ]

        """
        return self._client.patch(
            f"{self._base_api}/policy_groups",
            json={'policyGroups': policy_groups}
        )        

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
