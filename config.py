import os

class Config(object):
    """Environment Variables Configuration.
    Any added environment variable will be accessible from 
    an dict (app.config['ENV_VARIABLE_NAME']).
    """
    DEEPL_SECRET_KEY = os.environ.get('DEEPL_SECRET_KEY')