from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @property
    def async_db_connection_url(self):
        return "postgresql+psycopg://{}:{}@{}:{}/{}".format(
            self.DB_USER, self.DB_PASSWORD,
            self.DB_HOST, self.DB_PORT, self.DB_NAME
        )

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
