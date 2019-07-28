import os


class BaseConfig():
    DEBUG = False
    DATABASE_URL = os.environ.get('DATABASE_URL')


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass


configurations = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
