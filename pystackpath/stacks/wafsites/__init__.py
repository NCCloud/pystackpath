from pystackpath.util import BaseSite
from pystackpath.stacks.wafsites.api_login_urls import ApiLoginUrls
from pystackpath.stacks.wafsites.api_urls import ApiUrls
from pystackpath.stacks.wafsites.ddos import Ddos
from pystackpath.stacks.wafsites.monitoring import Monitoring
from pystackpath.stacks.wafsites.policy_groups import PolicyGroups
from pystackpath.stacks.wafsites.rules import Rules


class WafSites(BaseSite):
    def rules(self):
        return Rules(self._client, f"{self._base_api}/sites/{self.id}")

    def ddos(self):
        return Ddos(self._client, f"{self._base_api}/sites/{self.id}")

    def policy_groups(self):
        return PolicyGroups(self._client, f"{self._base_api}/sites/{self.id}")

    def api_login_urls(self):
        return ApiLoginUrls(self._client, f"{self._base_api}/sites/{self.id}")

    def api_urls(self):
        return ApiUrls(self._client, f"{self._base_api}/sites/{self.id}")

    def monitoring(self):
        return Monitoring(self._client, f"{self._base_api}/sites/{self.id}")
