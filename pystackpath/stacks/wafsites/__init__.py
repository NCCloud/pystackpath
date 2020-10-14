from pystackpath.util import BaseSite
from pystackpath.stacks.wafsites.api_login_urls import ApiLoginUrls
from pystackpath.stacks.wafsites.api_urls import ApiUrls
from pystackpath.stacks.wafsites.ddos import Ddos
from pystackpath.stacks.wafsites.monitoring import Monitoring
from pystackpath.stacks.wafsites.policy_groups import PolicyGroups
from pystackpath.stacks.wafsites.rules import Rules
from pystackpath.stacks.wafsites.events import Events
from pystackpath.stacks.wafsites.requests import Requests
from pystackpath.stacks.wafsites.traffic import Traffic
from pystackpath.stacks.wafsites.traffic_v2 import Traffic as TrafficV2


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

    def set_monitoring(self):
        return Monitoring(self._client, f"{self._base_api}/sites/{self.id}")

    def events(self):
        return Events(self._client, f"{self._base_api}/sites/{self.id}")

    def requests(self):
        return Requests(self._client, f"{self._base_api}/sites/{self.id}") 

    def traffic(self):
        '''
        deprecated
        '''
        return Traffic(self._client, f"{self._base_api}")          


class WafSitesV2(BaseSite):
    def traffic(self):
        return TrafficV2(self._client, f"{self._base_api}") 