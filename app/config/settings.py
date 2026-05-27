from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # =========================
    # APIs
    # =========================

    TEXT_MODEL_API: str
    IMAGE_MODEL_API: str

    TEXT_API_TIMEOUT: int
    IMAGE_API_TIMEOUT: int

    # =========================
    # MYSQL
    # =========================

    MYSQL_HOST: str
    MYSQL_PORT: int

    MYSQL_DATABASE: str

    MYSQL_USER: str
    MYSQL_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()