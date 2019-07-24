import os


class BaseConfig():
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DATABASE_URL = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    pass


configurations = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
