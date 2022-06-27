# configs.py
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, Field, BaseModel


class AppConfig(BaseModel):
    """Application configurations."""

    VAR_A: int = 33
    VAR_B: float = 22.0

    # all the directory level information defined at app config level
    # we do not want to pollute the env level config with these information
    # this can change on the basis of usage

    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    SETTINGS_DIR: Path = BASE_DIR.joinpath("settings")
    SETTINGS_DIR.mkdir(parents=True, exist_ok=True)

    LOGS_DIR: Path = BASE_DIR.joinpath("logs")
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    MODELS_DIR: Path = BASE_DIR.joinpath("models")
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    # local cache directory to store images or text file
    CACHE_DIR: Path = BASE_DIR.joinpath("cache")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    # question classification model to use
    CLASSIFICATION_MODEL: Path = MODELS_DIR.joinpath("question_classification.sav")


class GlobalConfig(BaseSettings):
    """Global configurations."""

    # These variables will be loaded from the .env file. However, if
    # there is a shell environment variable having the same name,
    # that will take precedence.

    APP_CONFIG: AppConfig = AppConfig()

    API_NAME: Optional[str] = Field(None, env="API_NAME")
    API_DESCRIPTION: Optional[str] = Field(None, env="API_DESCRIPTION")
    API_VERSION: Optional[str] = Field(None, env="API_VERSION")
    API_DEBUG_MODE: Optional[bool] = Field(None, env="API_DEBUG_MODE")

    # define global variables with the Field class
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    # logging configuration file
    LOG_CONFIG_FILENAME: Optional[str] = Field(None, env="LOG_CONFIG_FILENAME")

    MODEL_CONFIG_FILENAME: Optional[str] = Field(None, env="MODEL_CONFIG_FILENAME")
    MODEL_CONFIGS = ""

    DEV_MONGO_DB : Optional[str] = Field(None, env="DEV_MONGO_DB")
    DEV_POSTGRESQL_DB : Optional[str] = Field(None, env="DEV_POSTGRESQL_DB")
    DEV_INFLUX_DB : Optional[str] = Field(None, env="DEV_INFLUX_DB")

    # environment specific variables do not need the Field class
    HOST: Optional[str] = None
    PORT: Optional[int] = None
    LOG_LEVEL: Optional[str] = None

    DB: Optional[str] = None

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"


class DevConfig(GlobalConfig):
    """Development configurations."""

    class Config:
        env_prefix: str = "DEV_"


class ProdConfig(GlobalConfig):
    """Production configurations."""

    class Config:
        env_prefix: str = "PROD_"


class FactoryConfig:
    """Returns a config instance depending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()

        elif self.env_state == "prod":
            return ProdConfig()


def loadModelConfigs():
    from application.main.utility.config_loader import ConfigReaderInstance
    config = ConfigReaderInstance.yaml.read_config_from_file(
        settings.MODEL_CONFIG_FILENAME
    )
    return config.__dict__['models']
    

settings = FactoryConfig(GlobalConfig().ENV_STATE)()
settings.MODEL_CONFIGS = loadModelConfigs()
