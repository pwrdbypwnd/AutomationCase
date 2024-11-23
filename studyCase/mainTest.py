import unittest

from driver import DriverHelper
from helpers.utils import take_screenshot
from pages.careers_page import CareersPage
from pages.home_page import HomePage



class TestInsider(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize WebDriver
        cls.driver = DriverHelper.get_driver()
        # Initialize page objects
        cls.home_page = HomePage(cls.driver)
        cls.careers_page = CareersPage(cls.driver)

    def test_home_page_logo(self):
        try:
            # Open Insider homepage
            self.driver.get("https://useinsider.com/")
            # Verify homepage logo visibility
            self.assertTrue(self.home_page.verify_logo_visibility(), "Logo not visible!")
            # Take screenshot on success
            take_screenshot(self.driver, "test_home_page_logo", success=True)
        except Exception as e:
            # Take screenshot on failure
            take_screenshot(self.driver, "test_home_page_logo", success=False)
            raise e

    def test_navigate_to_careers(self):
        try:
            # Navigate to Careers page
            self.home_page.navigate_to_careers()
            # Verify blocks (Locations, Teams, Life at Insider) are visible
            self.assertTrue(
                self.careers_page.verify_blocks_visibility(),
                "One or more blocks are not visible!"
            )
            # Take screenshot on success
            take_screenshot(self.driver, "test_navigate_to_careers", success=True)
        except Exception as e:
            # Take screenshot on failure
            take_screenshot(self.driver, "test_navigate_to_careers", success=False)
            raise e

    @classmethod
    def tearDownClass(cls):
        # Quit the WebDriver session
        cls.driver.quit()
