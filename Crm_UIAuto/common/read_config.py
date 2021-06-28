import configparser
import os

# conf_path = os.path.join(os.path.dirname(__file__), '../conf/config.ini')

conf_path = os.path.dirname(os.path.abspath(__file__))

class ReadConfig(object):

    def __init__(self):
        #读取配置文件
        self.config = configparser.ConfigParser()
        self.config.read(conf_path, 'config.ini')

    def get_url(self):
        return self.config.get('default', 'url')

    def get_driver(self):
        return self.config.get('default', 'driver')

    def get_username(self):
        return self.config.get('default', 'username')

    def get_password(self):
        return self.config.get('default', 'password')

    @property
    def get_element_path(self):
        return self.config.get('default', 'element_path')


if __name__ == "__main__":
    local_config = ReadConfig()
    a = local_config.get_element_path()
    print(a)
