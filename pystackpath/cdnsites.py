from .util import BaseObject, PageInfo, pagination_query


class CdnSites(BaseObject):
    def index(self, first="", after="", filter="", sort_by=""):
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get("/cdn/v1/stacks/{}/sites".format(self._parent_id), params=pagination)
        response.raise_for_status()
        items = []
        for item in response.json()["results"]:
            items.append(self.loaddict(item))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def get(self, site_id):
        response = self._client.get("/cdn/v1/stacks/{}/sites/{}".format(self._parent_id, site_id))
        response.raise_for_status()
        return self.loaddict(response.json()["site"])

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
        response = self._client.post(
            "/cdn/v1/stacks/{}/sites".format(self._parent_id),
            json=payload
        )
        response.raise_for_status()
        return self.loaddict(response.json()["site"])

    def delete(self):
        """
        Delete a CDN site
        :return: a stackpath site object with the deleted cdn site
        """
        response = self._client.delete("/cdn/v1/stacks/{}/sites/{}".format(self._parent_id, self.id))
        response.raise_for_status()
        return self

    def disable(self):
        """
        Disable a CDN site
        :return: a stackpath site object with the disabled cdn site
        """
        response = self._client.post("/cdn/v1/stacks/{}/sites/{}/disable".format(self._parent_id, self.id))
        response.raise_for_status()
        return self

    def enable(self):
        """
        Enable a CDN site
        :return: a stackpath site object with the enabled cdn site
        """
        response = self._client.post("/cdn/v1/stacks/{}/sites/{}/enable".format(self._parent_id, self.id))
        response.raise_for_status()
        return self
