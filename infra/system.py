import os


def get_hostname():
    return os.uname()[1]
