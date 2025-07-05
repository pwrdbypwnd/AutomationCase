import unittest
from driver import DriverHelper
from pages import InsiderPage
from helpers import take_screenshot

class TestInsider(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverHelper.get_driver()
        cls.insider_page = InsiderPage(cls.driver)

    def test_home_page_logo(self):
        self.insider_page.open_home_page()
        try:
            self.assertTrue(
                self.insider_page.verify_home_page_logo(),
                "Main page appearance failed!"
            )
            take_screenshot(self.driver, "test_home_page_logo", success=True)
        except Exception as e:
            take_screenshot(self.driver, "test_home_page_logo", success=False)
            raise e

    def test_home_page_title(self):
        self.insider_page.open_home_page()
        expected_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
        try:
            self.assertTrue(
                self.insider_page.verify_page_title(expected_title),
                f"Unmatched failed, expected : {expected_title}"
            )
            take_screenshot(self.driver, "test_home_page_title", success=True)
        except Exception as e:
            take_screenshot(self.driver, "test_home_page_title", success=False)
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
