from configparser import ConfigParser
from pathlib import Path

def readConfig(section, key):
    config = ConfigParser()
    # config.read(".\\ConfigurationData\\conf.ini")
    config.read(str(Path().absolute().parent) + "\\ConfigurationData\\conf.ini")
    return config.get(section, key)


