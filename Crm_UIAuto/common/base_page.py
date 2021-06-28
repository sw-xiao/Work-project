from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    #获取定位元素的方法
    def find_element(self, element_info):
        element_name = element_info['element_name']
        locator_type = element_info['locator_type']
        locator_value = element_info['locator_value']
        timeout = element_info['timeout']
        if locator_type == 'id':
            locator_type = By.ID
        elif locator_type == 'name':
            locator_type = By.NAME
        elif locator_type == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type == 'xpath':
            locator_type = By.XPATH
        elif locator_type == 'css':
            locator_type = By.CSS_SELECTOR
        elif locator_type == 'link':
            locator_type = By.LINK_TEXT
        element = WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(locator_type, locator_value))
        return element

