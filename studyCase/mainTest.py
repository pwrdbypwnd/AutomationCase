import time
import unittest

from studyCase.pages.home_page import HomePage
from studyCase.pages.careers_page import CareersPage
from studyCase.pages.base import BasePage
from studyCase.helpers.utils import take_screenshot

from driver import DriverHelper

def set_browser_size(driver, width=1024, height=768):
    driver.set_window_size(width, height)
    print(f"Browser resized to: {width}x{height}")

def maximize_browser(driver):
    driver.maximize_window()

class TestInsider(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverHelper.get_driver()
        cls.home_page = HomePage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.careers_page = CareersPage(cls.driver)

    def test_home_page_logo(self):
        self.driver.get("https://useinsider.com/")
        try:
       #     expected_title = "# 1 Leader in Individualized, Cross-Channel CX — Insider"

       #     self.assertTrue(
       #         self.home_page.verify_title(expected_title),
       #         f"Expected title '{expected_title}' does not match!"
       #     )
            self.assertTrue(self.home_page.verify_logo_visibility(), "Logo is not visible!")
            take_screenshot(self.driver, "test_home_page_logo", success=True)
        except Exception as e:
            take_screenshot(self.driver, "test_home_page_logo", success=False)
            raise e

    def test_navigate_to_careers(self):
        try:
            self.home_page.navigate_to_careers()
            self.assertIn("careers", self.driver.current_url, "Navigation to Careers page failed!")
            take_screenshot(self.driver, "test_navigate_to_careers", success=True)
        except Exception as e:
            take_screenshot(self.driver, "test_navigate_to_careers", success=False)
            raise e

    def test_navigate_to_quality_assurance(self):
        try:
            expected_title = "Ready to disrupt? | Insider Careers"
            self.assertTrue(
                self.base_page.verify_title(expected_title),
                f"Expected title '{expected_title}' does not match!"
            )

            self.careers_page.expand_teams_section()
            self.careers_page.click_quality_assurance()
            take_screenshot(self.driver, "test_navigate_to_quality_assurance", success=True)
        except Exception as e:
            take_screenshot(self.driver, "test_navigate_to_quality_assurance", success=False)
            raise e

    def test_quality_assurance_jobs(self):
        try:
            qa_page_title = "Insider quality assurance job opportunities"
            self.assertTrue(
                self.base_page.verify_title(qa_page_title),
                f"Page title mismatch: expected '{qa_page_title}'"
            )

            self.careers_page.click_see_all_qa_jobs()

            take_screenshot(self.driver, "test_quality_assurance_jobs", success=True)
        except Exception as e:
            take_screenshot(self.driver, "test_quality_assurance_jobs", success=False)
            raise e

    def test_y_dropdown_interaction(self):
        try:
            open_position_page_title = "Insider Open Positions | Insider"
            self.assertTrue(
                self.base_page.verify_title(open_position_page_title),
                f"Page title mismatch: expected '{open_position_page_title}'"
            )
            self.driver.refresh()
            time.sleep(10)
            self.careers_page.click_department()
            self.careers_page.select_department("Quality Assurance")
            take_screenshot(self.driver, "test_z_dropdown_interactionLocation", success=True)


            self.careers_page.click_location()
            self.careers_page.select_location("Istanbul, Turkey")
            take_screenshot(self.driver, "test_z_dropdown_interactionDepartment", success=True)

            time.sleep(1)
            self.careers_page.print_total_result()
            take_screenshot(self.driver, "test_z_dropdown_interactionResult", success=True)

        except Exception as e:
            take_screenshot(self.driver, "test_z_dropdown_interaction", success=False)
            print(f"test_y_dropdown_interaction failed")
            raise e

    def test_z_view_role(self):
        try:
            self.careers_page.view_role_button("https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc")
            take_screenshot(self.driver, "resultCounterRedirectedPage", success=True)

        except Exception as e:
            take_screenshot(self.driver, "resultCounterRedirectedPage", success=False)
            print(f"test_z_view_role failed")
            raise e



    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
