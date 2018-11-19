import os

class Config(object):
    """
    Main configuration class
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")

class Testing(Config):
    """
    Testing Configurations
    """
    DEBUG = True
    TESTING = True

class Development(Config):
    """
    Development configurations
    """
    DEBUG = True

class Release(Config):
    """
    Configurations for release
    """
    TESTING = False
    DEBUG = False

config = {
    'testing' : Testing,
    'development' : Development,
    'release' : Release
}