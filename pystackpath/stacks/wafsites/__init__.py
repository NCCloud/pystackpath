from pystackpath.util import BaseSite
from pystackpath.stacks.wafsites.ddos import Ddos
from pystackpath.stacks.wafsites.policy_groups import PolicyGroups
from pystackpath.stacks.wafsites.rules import Rules


class WafSites(BaseSite):
    def rules(self):
        return Rules(self._client, f"{self._base_api}/sites/{self.id}")

    def ddos(self):
        return Ddos(self._client, f"{self._base_api}/sites/{self.id}")

    def policy_groups(self):
        return PolicyGroups(self._client, f"{self._base_api}/sites/{self.id}")
