from requests import Session, HTTPError

from .stacks import Stacks
from .config import BASE_URL


class OAuth2Session(Session):
    def __init__(self, clientid, apisecret, custom_hooks: list = []):
        self._clientid = clientid
        self._apisecret = apisecret
        self._custom_hooks = custom_hooks
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

    def _add_hooks(self, kwargs):
        if self._custom_hooks:
            if not "hooks" in kwargs:
                kwargs["hooks"] = dict()
            if not "response" in kwargs["hooks"]:
                kwargs["hooks"]["response"] = list()

            kwargs["hooks"]["response"] = kwargs["hooks"]["response"] + self._custom_hooks

        return kwargs

    def request(self, method, url, **kwargs):
        kwargs = self._add_auth(kwargs)
        kwargs = self._add_hooks(kwargs)
        response = super(OAuth2Session, self).request(method, BASE_URL + url, **kwargs)
        if response.status_code == 401:
            self._refresh_token()
            kwargs = self._add_auth(kwargs)
            kwargs = self._add_hooks(kwargs)
            response = super(OAuth2Session, self).request(method, BASE_URL + url, **kwargs)
        return response


class Stackpath(object):
    _clientid = ""
    _apisecret = ""

    client = None

    def __init__(self, clientid, apisecret, custom_hooks: list = []):
        self._clientid = clientid
        self._apisecret = apisecret
        self._init_client(custom_hooks)

    def _init_client(self, custom_hooks):
        self.client = OAuth2Session(self._clientid, self._apisecret, custom_hooks=custom_hooks)

    def stacks(self):
        return Stacks(self.client)
