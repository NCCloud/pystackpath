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
                 endCursor=""
    ):
        self.totalCount = totalCount
        self.hasPreviousPage = hasPreviousPage
        self.hasNextPage = hasNextPage
        self.startCursor = startCursor
        self.endCursor = endCursor


class BaseObject(object):
    _client = None

    def __init__(self, client, parent_id=0):
        self._client = client
        self._parent_id = parent_id

    @classmethod
    def newinstance(cls, client, parent_id=0):
        instance = cls(client, parent_id)
        return instance

    def loaddict(self, d):
        instance = self.newinstance(self._client, self._parent_id)
        for key, value in d.items():
            setattr(instance, key, value)
        return instance


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
