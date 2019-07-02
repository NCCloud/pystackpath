from .util import PageInfo, pagination_query


class Stacks(object):
    _client = None

    id = ""
    accountId = ""
    name = ""
    createdAt = ""
    updatedAt = ""
    status = ""

    def __init__(self, client,
                 id="",
                 accountId="",
                 name="",
                 createdAt="",
                 updatedAt="",
                 status=""
    ):
        self._client = client
        self.id = id
        self.accountId = accountId
        self.name = name
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.status = status

    @classmethod
    def fromdict(cls, client, d):
        return cls(client, **d)

    def index(self, first="", after="", filter="", sort_by=""):
        pagination = pagination_query(first=first, after=after, filter=filter, sort_by=sort_by)
        response = self._client.get("/stack/v1/stacks", params=pagination)

        items = []
        for item in response.json()["results"]:
            items.append(self.fromdict(self._client, item))
        pageinfo = PageInfo(**response.json()["pageInfo"])

        return items, pageinfo

    def get(self, stack_id):
        response = self._client.get("/stack/v1/stacks/%s" % stack_id)
        return self.fromdict(self._client, response.json())

    def create(self, accountid, name):
        response = self._client.post("/stack/v1/stacks",
                                     json={"accountId": accountid, "name": str(name)})
        return self.fromdict(self._client, response.json()["stack"])
