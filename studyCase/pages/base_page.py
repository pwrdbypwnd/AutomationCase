from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def click_element(self, by, locator):
        element = self.wait_for_element(by, locator)
        element.click()

    def get_element_text(self, by, locator):
        element = self.wait_for_element(by, locator)
        return element.text

    def is_element_visible(self, by, locator):
        try:
            self.wait_for_element(by, locator)
            return True
        except:
            return False
