from pystackpath.util import BaseObject


class Policies(BaseObject):
    def index(self):
        """
        Retrieve all policies in a WAF policy group
        :return: a list of policies in a WAF policy group
        """
        response = self._client.get(f"{self._base_api}/policies")
        items = [self.loaddict(item) for item in response.json()["policies"]]

        return items

    def get(self, policy_id):
        """
        Retrieve an individual WAF policy
        :param policy_id: The ID of the WAF policy to retrieve
        """
        response = self._client.get(f"{self._base_api}/policies/{policy_id}")
        return self.loaddict(response.json()["policy"])

    def enable(self):
        """
        Enable a WAF policy
        """
        response = self._client.post(f"{self._base_api}/policies/{self.id}/enable")

    def disable(self):
        """
        Disable a WAF policy
        """
        response = self._client.post(f"{self._base_api}/policies/{self.id}/disable")
