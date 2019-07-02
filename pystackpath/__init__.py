from requests import Session

from .stacks import Stacks
from .config import BASE_URL


class OAuth2Session(Session):
    def __init__(self, clientid, apisecret):
        self._clientid = clientid
        self._apisecret = apisecret
        self._token = ""

        super(OAuth2Session, self).__init__()

    def _refresh_token(self):
        response = super(OAuth2Session, self).post(
            "/identity/v1/oauth2/token",
            json={
                "grant_type": "client_credentials",
                "client_id": self._clientid,
                "client_secret": self._apisecret
            }
        )

        self._token = response.json()["access_token"]

    def _add_auth(self, kwargs):
        if not "headers" in kwargs:
            kwargs["headers"] = dict()
        kwargs["headers"]["Authorization"] = "Bearer %s" % self._token
        return kwargs

    def request(self, method, url, **kwargs):
        kwargs = self._add_auth(kwargs)
        response = super(OAuth2Session, self).request(method, BASE_URL + url, **kwargs)
        if response.status_code == 401:
            self._refresh_token()
            kwargs = self._add_auth(kwargs)
            response = super(OAuth2Session, self).request(method, BASE_URL + url, **kwargs)
        return response


class Stackpath(object):
    _clientid = ""
    _apisecret = ""
    _accountid = ""
    _token = {
        'access_token': 'eswfld123kjhn1v5423',
        'refresh_token': 'asdfkljh23490sdf',
        'token_type': 'Bearer',
        'expires_in': '-30',
    }
    _refresh_url = "{}/identity/v1/oauth2/token".format(BASE_URL)

    client = None

    def __init__(self, clientid, apisecret):
        self._clientid = clientid
        self._apisecret = apisecret
        self._init_client()
        self._init_stacks()

    def _init_client(self):
        self.client = OAuth2Session(self._clientid,self._apisecret)

    def _init_stacks(self):
        self.stacks = Stacks(self.client)

    def _token_saver(self, token):
        self._token = token
