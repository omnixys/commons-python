from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class JwtPayloadClaims(BaseModel):
    model_config = ConfigDict(extra="allow")
    iss: str | None = None
    sub: str | None = None
    aud: str | list[str] | None = None
    exp: int | None = None
    nbf: int | None = None
    iat: int | None = None
    jti: str | None = None


class KeycloakTokenPayload(JwtPayloadClaims):
    model_config = ConfigDict(extra="allow")
    sub: str | None = None
    username: str = ""
    first_name: str | None = Field(default=None, alias="first_name")
    last_name: str | None = Field(default=None, alias="last_name")
    email: str = ""
    email_verified: bool | None = Field(default=None, alias="email_verified")
    realm_access: dict[str, list[str]] | None = Field(default=None, alias="realm_access")
    azp: str | None = None


class KeycloakToken(BaseModel):
    model_config = ConfigDict(extra="allow")
    access_token: str = Field(alias="access_token")
    expires_in: int = Field(alias="expires_in")
    refresh_token: str = Field(alias="refresh_token")
    refresh_expires_in: int = Field(alias="refresh_expires_in")
    id_token: str = Field(alias="id_token")
    scope: str
