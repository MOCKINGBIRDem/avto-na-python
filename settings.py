from pydantic import BaseModel, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from os import path

ENV_FILE = path.join(path.dirname(__file__), '.env')


class BaseConfig(BaseModel):
    base_url: HttpUrl
    base_timeout: float


class UserConfig(BaseModel):
    username: str
    user_password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, env_file_encoding="utf-8", env_nested_delimiter=".")

    base_settings: BaseConfig
    user_settings: UserConfig


settings = Settings()

