from pydantic import Field
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    host: str = Field("127.0.0.1", alias="APP_HOST")
    port: int = Field(8000, alias="APP_PORT")
    reload: bool = Field(True, alias="APP_RELOAD")


def load_app_config() -> AppConfig:
    return AppConfig.model_construct()
