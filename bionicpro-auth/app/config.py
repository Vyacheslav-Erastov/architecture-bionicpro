from cryptography.fernet import Fernet

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    keycloak_url: str = Field("http://localhost:8080", env="KEYCLOAK_URL")
    keycloak_realm: str = Field("reports-realm", env="KEYCLOAK_REALM")
    client_id: str = Field("reports-frontend", env="CLIENT_ID")
    client_secret: str | None = Field(None, env="CLIENT_SECRET")
    auth_url: str = Field("http://localhost:8000", env="AUTH_URL")
    redirect_path: str = Field("auth/callback", env="REDIRECT_PATH")
    logout_redirect_path: str = Field(
        "auth/logout/callback", env="LOGOUT_REDIRECT_PATH"
    )
    frontend_url: str = Field("http://localhost:3000", env="FRONTEND_URL")

    redis_url: str = Field("redis://session_db:6379", env="REDIS_URL")
    session_ttl: int = 1800
    access_token_leeway: int = 120

    encryption_key: bytes = Field(Fernet.generate_key(), env="ENCRYPTION_KEY")

    class Config:
        env_file = ".env"


settings = Settings()
