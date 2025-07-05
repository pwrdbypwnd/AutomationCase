from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import InsiderLocators

class InsiderPage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):
        self.driver.get("https://useinsider.com/")

    def verify_home_page_logo(self):
        try:
            logo = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, InsiderLocators.HOMEPAGE_LOGO))
            )
            return logo.is_displayed()
        except Exception as e:
            print(f"Logo bulunamadı veya görünür değil: {e}")
            return False

    def verify_page_title(self, expected_title):
        try:
            actual_title = self.driver.title
            return actual_title == expected_title
        except Exception as e:
            print(f"Header check failed : {e}")
            return False
