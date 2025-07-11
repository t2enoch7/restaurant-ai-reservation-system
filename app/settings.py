from pydantic import BaseSettings


class Settings(BaseSettings):
    app_env: str = "development"
    dynamodb_endpoint: str
    reservation_table: str

    class Config:
        env_file = ".env"


settings = Settings()
