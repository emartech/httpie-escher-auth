"""
EscherAuth auth plugin for HTTPie.

"""
from httpie.plugins import AuthPlugin
import escherauth
import datetime
from urlparse import urlparse

__version__ = '0.2.2'
__author__ = 'Andras Barthazi'
__licence__ = 'MIT'

class EscherAuth:
    def __init__(self, escher_key, escher_secret):
        options = {}

        credential_scope = "escher_request"
        if "/" in escher_key:
            scope = escher_key.split("/")
            escher_key = scope.pop()
            credential_scope = "/".join(scope)

        self.client = {'api_key': escher_key, 'api_secret': escher_secret}
        self.escher = escherauth.Escher(credential_scope, options)

    def __call__(self, r):
        now = datetime.datetime.utcnow()
        r.headers['X-Escher-Date'] = now.strftime('%Y%m%dT%H%M%SZ')
        parsed_uri = urlparse(r.url)
        r.headers['Host'] = parsed_uri.netloc
        headers_to_sign = map(lambda x:x.lower(),r.headers.keys())
        headers_to_sign = [header for header in headers_to_sign if header not in ['accept', 'accept-encoding', 'user-agent', 'connection', 'content-type', 'content-length']]
        return self.escher.sign(r, self.client, headers_to_sign)

class EscherAuthPlugin(AuthPlugin):

    name = 'EscherAuth auth'
    auth_type = 'escher-auth'
    description = 'Sign Escher requests using the default Escher settings'

    def get_auth(self, access_id, secret_key):
        return EscherAuth(access_id, secret_key)
