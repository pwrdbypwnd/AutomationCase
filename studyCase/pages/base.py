
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def click_element(self, by, locator):
        element = self.wait_for_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
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

    def verify_title(self, expected_title):
        try:
            print(self.driver.title)
            return self.driver.title == expected_title
        except Exception as e:
            raise Exception(f"Failed to verify the title: {e}")

    def wait_for_element_to_be_present(self, by, locator, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, locator))
                )
        except Exception as e:
            raise Exception(f"Element with locator ({by}, {locator}) not present within {timeout} seconds")

    def wait_for_element_to_be_visible(self, by, locator, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
        except Exception as e:
            raise Exception(f"Element with locator ({by}, {locator}) not visible within {timeout} seconds")

    def wait_for_page_load(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
        except Exception as e:
            raise Exception(f"Page did not load within {timeout} seconds")

    def wait_for_element_to_be_clickable(self, by, locator, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            return element
        except TimeoutException:
            raise Exception(f"Element with locator ({by}, {locator}) not clickable within {timeout} seconds")

