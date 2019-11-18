class PageInfo(object):
    totalCount: str
    hasPreviousPage: bool
    hasNextPage: str
    startCursor: str
    endCursor: str

    def __init__(self, totalCount="",
                 hasPreviousPage=False,
                 hasNextPage="",
                 startCursor="",
                 endCursor=""):
        self.totalCount = totalCount
        self.hasPreviousPage = hasPreviousPage
        self.hasNextPage = hasNextPage
        self.startCursor = startCursor
        self.endCursor = endCursor


class BaseObject(object):
    _client = None
    _base_api = ""

    def __init__(self, client, base_api: str = ""):
        self._client = client
        self._base_api = base_api

    @classmethod
    def newinstance(cls, client, base_api: str = ""):
        instance = cls(client, base_api)
        return instance

    def loaddict(self, d):
        instance = self.newinstance(self._client, self._base_api)
        for key, value in d.items():
            setattr(instance, key, value)
        return instance

    def dumpdict(self) -> dict:
        d = dict()
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                d[key] = value
        return d


class BaseSite(BaseObject):
    def index(self, first="", after="", filter="", sort_by=""):
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get(f"{self._base_api}/sites", params=pagination)
        response.raise_for_status()
        items = []
        for item in response.json()["results"]:
            items.append(self.loaddict(item))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return {"results": items, "pageinfo": pageinfo}

    def get(self, site_id):
        response = self._client.get(f"{self._base_api}/sites/{site_id}")
        response.raise_for_status()
        return self.loaddict(response.json()["site"])

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
        response = self._client.post(f"{self._base_api}/sites", json=payload)
        response.raise_for_status()
        return self.loaddict(response.json()["site"])

    def delete(self):
        """
        Delete a CDN site
        :return: a stackpath site object with the deleted cdn site
        """
        response = self._client.delete(f"{self._base_api}/sites/{self.id}")
        response.raise_for_status()
        return self


def pagination_query(first="", after="", filter="", sort_by=""):
    params = dict()
    if first != "":
        params["page_request.first"] = first
    if after != "":
        params["page_request.after"] = after
    if filter != "":
        params["page_request.filter"] = filter
    if sort_by != "":
        params["page_request.first"] = sort_by

    return params


time_format = "%Y-%m-%dT%H:%M:%SZ"


def api_time_format(datetime_object):
    return datetime_object.strftime(time_format)


def dt_time_format(datetime_string):
    from datetime import datetime

    return datetime.strptime(datetime_string, time_format)
