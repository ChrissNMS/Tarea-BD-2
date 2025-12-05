"""Application configuration using Pydantic Settings."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Main application settings."""
    debug: bool = False
    jwt_secret: str = "secret123"
    jwt_secret_key: str = "super-secret-key"

    database_url: str = "mysql+pymysql://root:password@localhost:3306/library_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
