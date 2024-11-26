from studyCase.helpers.utils import take_screenshot
from studyCase.pages.base import BasePage
from studyCase.pages.locators import HomePageLocators

class HomePage(BasePage):
    def verify_logo_visibility(self):
        take_screenshot(self.driver, "verify_logo_visibility", success=True)
        return self.is_element_visible(*HomePageLocators.LOGO)

    def navigate_to_careers(self):
        self.click_element(*HomePageLocators.COMPANY_XPATH)
        take_screenshot(self.driver, "COMPANY_XPATH", success=True)
        self.click_element(*HomePageLocators.CAREERS_XPATH)
        take_screenshot(self.driver, "CAREERS_XPATH", success=True)