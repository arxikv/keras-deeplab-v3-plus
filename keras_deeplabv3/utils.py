import os


def prefix_home_keras(path):
    return os.path.join(os.path.expanduser('~'), '.keras', path)
