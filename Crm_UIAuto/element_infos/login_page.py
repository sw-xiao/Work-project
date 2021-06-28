from common import base_page
from common.element_infos_utils import ElementInfos
from common.read_config import local_config

class Login_Page(base_page.BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        element_data = ElementInfos(local_config.get_element_path, 'login_element').get_element_info()
        self.username_inputbox = element_data['username_inputbox']


if __name__ == '__main__':
    element_data = ElementInfos(local_config.get_element_path, 'login_element').get_element_info()
    print(element_data)