import configparser   # This is a inbuilt package in python

config = configparser.RawConfigParser()  # RawConfigParser() is a class inside the package
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod    # we can access these methods using class name without creating object
    def getAppURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getUserPassword():
        password=config.get('common info','password')
        return password

