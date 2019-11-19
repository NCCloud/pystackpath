from pystackpath.stacks.cdnsites.scopes import Scopes
from pystackpath.stacks.certificates import Certificates
from pystackpath.util import BaseSite


class CdnSites(BaseSite):
    def index(self, first="", after="", filter="", sort_by=""):
        return super(CdnSites, self).index(first="", after="", filter="", sort_by="")

    def get(self, site_id):
        return super(CdnSites, self).get(site_id)

    def create(self, **payload):
        """
        Create a new CDN site
        :param payload: dict according to https://stackpath.dev/reference/sites-2#createsite
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
        Boolean	enabled    Whether or not a site's CDN service is enabled.
        String	type       A CDN site's type.
                           A site's type determines how StackPath delivers content to incoming HTTP(S) requests.
                           UNKNOWN: StackPath is unable to determine a site's type
                           CDN: A site is CDN only site
                           WAF: A site is either a standalone WAF site or a WAF site with attached CDN service
                           API: A site is an API delivery site. API delivery sites are powered by both the WAF and CDN
                                and have custom rulesets for each.
        """
        return super(CdnSites, self).create(**payload)

    def delete(self):
        """
        Delete a CDN site
        :return: a stackpath site object with the deleted cdn site
        """
        return super(CdnSites, self).delete()

    def disable(self):
        """
        Disable a CDN site
        :return: a stackpath site object with the disabled cdn site
        """
        response = self._client.post(f"{self._base_api}/sites/{self.id}/disable")
        response.raise_for_status()
        return self

    def enable(self):
        """
        Enable a CDN site
        :return: a stackpath site object with the enabled cdn site
        """
        response = self._client.post(f"{self._base_api}/sites/{self.id}/enable")
        response.raise_for_status()
        return self

    def assign_certificate(self, certificate: Certificates):
        """
        Assign (and eventually force) a Certificate for the current Site.
        :param certificate:
        :return:
        """
        response = self._client.put(f"{self._base_api}/sites/{self.id}/certificates/{certificate.id}")
        response.raise_for_status()

        certificate = Certificates(self._client, f"{self._base_api}/certificates")
        return certificate.loaddict(response.json()["siteCertificate"]["certificate"])

    def scopes(self):
        return Scopes(self._client, f"{self._base_api}/sites/{self.id}")
