import os
class Config:
    DEBUG=False
    CRSF_ENABLED=True
    SECRET=os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://anilla:Busolo@1997@localhost/test_db'

class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI='postgres://localhost/text_db'
    DEBUG=True

class StagingConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False
    TESTING=True

app_config={
'development':DevelopmentConfig,
'testing':TestingConfig,
'staging':StagingConfig,
'production':ProductionConfig
}
