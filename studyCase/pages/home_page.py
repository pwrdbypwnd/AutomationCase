from base_page import BasePage
from locators import HomePageLocators

class HomePage(BasePage):
    def verify_logo_visibility(self):
        return self.is_element_visible(*HomePageLocators.LOGO)

    def navigate_to_careers(self):
        self.click_element(*HomePageLocators.COMPANY_MENU)
        self.click_element(*HomePageLocators.CAREERS_MENU)
