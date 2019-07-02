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
