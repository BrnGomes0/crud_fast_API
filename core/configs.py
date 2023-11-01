from pydantic.v1 import BaseSetting
from sqlalchemy.orm import declarative_base

class Settings(BaseSetting):
    """
        Configurações gerais utilizadas em nossa aplicação!
    """

    API_V1_STR: str = 'api/v1'
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:3306/etscurso'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()