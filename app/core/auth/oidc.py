import os
from enum import Enum
import httpx
from fastapi.security import OpenIdConnect


class OIDCProvider(Enum):
    COGNITO = "cognito"


class OIDCConfiguration:
    def __init__(
        self,
        provider: OIDCProvider = OIDCProvider.COGNITO,        
    ):
            self.client_id = os.getenv("OIDC_CLIENT_ID")
            self.client_secret = os.getenv("OIDC_CLIENT_SECRET")
            self.authority = os.getenv("OIDC_AUTHORITY")
            self.redirect_uri = os.getenv("OIDC_REDIRECT_URI")
            self.provider = provider
            self.configuration_url = (
                f"{self.authority}/.well-known/openid-configuration"
            )
            json_config = httpx.get(self.configuration_url).json()
            self.authorization_endpoint = json_config.get("authorization_endpoint")
            self.userinfo_endpoint = json_config.get("userinfo_endpoint")
            self.token_endpoint = json_config.get("token_endpoint")
            self.jwks_keys = httpx.get(
                url=f"{self.authority}/.well-known/jwks.json"
            ).json()
            self.oidc_dependency = OpenIdConnect(
                openIdConnectUrl=self.configuration_url
            )
oidc = OIDCConfiguration()
