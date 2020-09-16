from pystackpath.stacks.zones.records import Records
from pystackpath.util import BaseObject, pagination_query, PageInfo


class Zones(BaseObject):
    def create(self, **payload):
        """
        Create a new zone
        :param payload: dict according to https://stackpath.dev/reference/zones#createzone
        :return: dict with DNS zone
        String	id          A zone's unique identifier.
        String	stackId     The ID of the stack to which a zone belongs.
        String	domain      A zone's name. Site names correspond to their fully-qualified domain name.
        String	version     A zone's version number. Version numbers are incremented automatically
                            when a zone is updated
        List	nameservers A zone's NS hostnames of resolvers that host a zone. Every zone has multiple
                            name servers assigned by StackPath upon creation for redundancy purposes.
        String	status      A zone's internal state. Zone status is controlled by StackPath as zones
                            are managed by StackPath's accounting and security teams.
        Boolean	disabled    A zone's disabled flag. Shows whether or not a zone has been disabled by
                            the user.
        String	createdAt   The date that a zone was created.
        String	updatedAt   The date that a zone was last updated.
        String	verified    The date that a zone's NSes were last audited by StackPath.
        dict	labels      The optional dict of zone's user labels. Zone labels are not processed by StackPath
                            and are solely used for users to organize their zones.
        """
        response = self._client.post(f"{self._base_api}/zones", json=payload)
        return self.loaddict(response.json()["zone"])

    def index(self, first="", after="", filter="", sort_by=""):
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get(f"{self._base_api}/zones", params=pagination)
        items = []
        for item in response.json()["zones"]:
            items.append(self.loaddict(item))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"zones": items, "pageinfo": pageinfo}

    def get(self, zone_id):
        response = self._client.get(f"{self._base_api}/zones/{zone_id}")
        return self.loaddict(response.json()["zone"])

    def delete(self):
        """
        Delete a zone
        :return: a stackpath zone object with the deleted zone
        """
        response = self._client.delete(f"{self._base_api}/zones/{self.id}")
        return self

    def disable(self):
        """
        Disable a zone
        :return: a stackpath site object with the disabled zone
        """
        response = self._client.post(f"{self._base_api}/zones/{self.id}/disable")
        return self

    def enable(self):
        """
        Enable a zone
        :return: a stackpath site object with the enabled zone
        """
        response = self._client.post(f"{self._base_api}/zones/{self.id}/enable")
        return self

    def update_labels(self, labels: dict):
        """
        Update a zone user labels
        :param labels:
        :return: dict with DNS zone
        String	id          A zone's unique identifier.
        String	stackId     The ID of the stack to which a zone belongs.
        String	domain      A zone's name. Site names correspond to their fully-qualified domain name.
        String	version     A zone's version number. Version numbers are incremented automatically
                            when a zone is updated
        List	nameservers A zone's NS hostnames of resolvers that host a zone. Every zone has multiple
                            name servers assigned by StackPath upon creation for redundancy purposes.
        String	status      A zone's internal state. Zone status is controlled by StackPath as zones
                            are managed by StackPath's accounting and security teams.
        Boolean	disabled    A zone's disabled flag. Shows whether or not a zone has been disabled by
                            the user.
        String	createdAt   The date that a zone was created.
        String	updatedAt   The date that a zone was last updated.
        String	verified    The date that a zone's NSes were last audited by StackPath.
        dict	labels      The optional dict of zone's user labels. Zone labels are not processed by StackPath
                            and are solely used for users to organize their zones.
        """
        response = self._client.put(f"{self._base_api}/zones/{self.id}", json={'labels': labels})
        return self.loaddict(response.json()["zone"])


    def records(self):
        return Records(self._client,  f"{self._base_api}/zones/{self.id}")
