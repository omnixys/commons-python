from __future__ import annotations

from pydantic import BaseModel, ConfigDict


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
    username: str
    first_name: str | None = None
    last_name: str | None = None
    email: str
    email_verified: bool | None = None
    realm_access: dict[str, list[str]] | None = None
    azp: str | None = None


class KeycloakToken(BaseModel):
    model_config = ConfigDict(extra="allow")
    access_token: str
    expires_in: int
    refresh_token: str
    refresh_expires_in: int
    id_token: str
    scope: str


class KeycloakRawOutput(BaseModel):
    model_config = ConfigDict(extra="allow")
    exp: int
    iat: int
    jti: str
    iss: str
    aud: list[str]
    sub: str
    typ: str = "Bearer"
    azp: str
    sid: str
    acr: str
    allowed_origins: list[str] | None = None
    realm_access: dict[str, list[str]] | None = None
    resource_access: dict[str, dict[str, list[str]]] | None = None
    scope: str
    email_verified: bool = False
    name: str | None = None
    preferred_username: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    email: str
