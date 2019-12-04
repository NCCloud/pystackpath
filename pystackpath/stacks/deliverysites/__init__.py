from pystackpath.util import BaseSite
from pystackpath.stacks.deliverysites.delivery_domain import DeliveryDomains


class DeliverySites(BaseSite):

    def create(self, **payload):
        """
        Create a new site
        :param payload: dict according to https://stackpath.dev/reference/sites#createsite-1
        :return: dict with created site
        String	id         A CDN site's unique identifier.
        String	stackId    The ID of the stack to which a CDN site belongs.
        String	label      A CDN site's name. Site names correspond to their fully-qualified domain name.
        String	status     A CDN site's internal state. Site status is controlled by StackPath as sites
                           are provisioned and managed by StackPath's accounting and security teams.
        String	createdAt  The date that a CDN site was created.
        String	updatedAt  The date that a CDN site was last updated.
        List	features   A CDN site's associated features.
                           Features control how StackPath provisions and configures a site.
        """
        return super(DeliverySites, self).create(**payload)

    def delete(self):
        """
        Delete a site
        :return: a stackpath site object with the deleted cdn site
        """
        return super(DeliverySites, self).delete()

    def disable_cdn(self):
        """
        Disable a CDN site
        :return: a stackpath site object with the disabled cdn site
        """
        response = self._client.delete(f"{self._base_api}/sites/{self.id}/cdn")
        return self

    def enable_cdn(self):
        """
        Enable a CDN site
        :return: a stackpath site object with the enabled cdn site
        """
        response = self._client.post(f"{self._base_api}/sites/{self.id}/cdn")
        return self

    def disable_waf(self):
        """
        Disable a WAF site
        :return: a stackpath site object with the disabled waf site
        """
        response = self._client.delete(f"{self._base_api}/sites/{self.id}/waf")
        return self

    def enable_waf(self):
        """
        Enable a WAF site
        :return: a stackpath site object with the enabled waf site
        """
        response = self._client.post(f"{self._base_api}/sites/{self.id}/waf")
        return self

    def disable_scripting(self):
        """
        Disable a SCRIPTING site
        :return: a stackpath site object with the disabled scripting site
        """
        response = self._client.delete(f"{self._base_api}/sites/{self.id}/scripting")
        return self

    def enable_scripting(self):
        """
        Enable a SCRIPTING site
        :return: a stackpath site object with the enabled scripting site
        """
        response = self._client.post(f"{self._base_api}/sites/{self.id}/scripting")
        return self

    def delivery_domains(self):
        return DeliveryDomains(self._client, f"{self._base_api}/sites/{self.id}")
