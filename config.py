import os


class Config(object):
    SECRET_KEY = os.environ.get(
        "SECRET_KEY") or b'T\xb7h^\xe8\xc29Ia$\xc7?\xfb\x0b\xa0\x13'

    MONGODB_SETTINGS = {'db': 'UTA_Enrollment'}
