import time
from selenium.webdriver.common.by import By
from studyCase.helpers.utils import take_screenshot

from studyCase.pages.base import BasePage
from studyCase.pages.locators import CareersPageLocators


class CareersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.careers_page = None

    def expand_teams_section(self):
        try:
            expand_button = self.wait_for_element(By.XPATH, CareersPageLocators.EXPAND_BUTTON_XPATH)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", expand_button)
            time.sleep(3)
            try:
                expand_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", expand_button)
        except Exception as e:
            take_screenshot(self.driver, "expand_teams_section", success=False)
            raise Exception(f"Failed to expand teams section")

    def click_quality_assurance(self):
        try:
            quality_assurance_button = self.wait_for_element(By.XPATH, CareersPageLocators.QUALITY_ASSURANCE_XPATH)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", quality_assurance_button)
            time.sleep(3)
            try:
                quality_assurance_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", quality_assurance_button)
        except Exception as e:
            take_screenshot(self.driver, "click_quality_assurance", success=False)
            raise Exception(f"Failed to click on Quality Assurance")


    def click_see_all_qa_jobs(self):
        try:
            qa_jobs_button = self.wait_for_element(By.XPATH, CareersPageLocators.SEE_ALL_QA_JOBS_XPATH)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", qa_jobs_button)
            time.sleep(3)
            try:
                qa_jobs_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", qa_jobs_button)
        except Exception as e:
            take_screenshot(self.driver, "click_see_all_qa_jobs", success=False)
            raise Exception(f"Failed to click 'See all QA jobs' button")

    def click_location(self):
        try:
            location_click_button = self.wait_for_element(By.ID, CareersPageLocators.FILTER_LOCATION_BY_ID)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", location_click_button)
            time.sleep(3)
            try:
                location_click_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", location_click_button)
        except Exception as e:
            take_screenshot(self.driver, "click_location", success=False)
            raise Exception(f"Failed to click 'Location Dropdown List' button")

    def click_department(self):
        try:
            department_click_button = self.wait_for_element(By.ID, CareersPageLocators.FILTER_DEPARTMENT_BY_ID)
            try:
                department_click_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", department_click_button)
        except Exception as e:
            take_screenshot(self.driver, "click_department", success=False)
            raise Exception(f"Failed to click 'Department Dropdown List' button")

    def select_location(self, option_text):
        try:
            option_xpath = f"//li[contains(@class, 'select2-results__option') and text()='{option_text}']"
            option_location = self.wait_for_element(By.XPATH, option_xpath)
            try:
                option_location.click()
            except:
                self.driver.execute_script("arguments[0].click();", option_location)
        except Exception as e:
            take_screenshot(self.driver, "select_location", success=False)
            raise Exception(f"Failed to click 'Location Dropdown List' button")

    def select_department(self, option_text):
        try:
            option_xpath = f"//li[contains(@class, 'select2-results__option') and text()='{option_text}']"
            option_department = self.wait_for_element(By.XPATH, option_xpath)
            try:
                option_department.click()
            except:
                self.driver.execute_script("arguments[0].click();", option_department)
        except Exception as e:
            take_screenshot(self.driver, "select_department", success=False)
            raise Exception(f"Failed to click 'Department Dropdown List' button")

    def print_total_result(self):
        try:
            time.sleep(5)
            total_result_element = self.wait_for_element(By.ID, CareersPageLocators.RESULT_COUNTER_ID)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", total_result_element)
            total_result_text = total_result_element.text

            print(f"Total Result: {total_result_text}")
        except Exception as e:
            take_screenshot(self.driver, "print_total_result", success=False)
            raise Exception(f"Failed to get total result")

    def view_role_button(self, expected_url):
        try:
            view_role_button = self.wait_for_element(By.XPATH, CareersPageLocators.VIEW_ROLE_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", view_role_button)
            href_value = view_role_button.get_attribute("href")
            assert href_value == expected_url, f"Expected URL '{expected_url}' does not match '{href_value}'"
            print(f"URL validation passed: {href_value}")

            try:
                view_role_button.click()
                self.driver.switch_to.window(self.driver.window_handles[-1])
                current_url = self.driver.current_url
                assert current_url == expected_url, f"Expected '{expected_url}' but got '{current_url}'"
                print(f"Navigated URL validation passed: {current_url}")
                take_screenshot(self.driver, "view_role_button", success=True)
            except:
                self.driver.execute_script("arguments[0].click();", view_role_button)
                take_screenshot(self.driver, "view_role_button", success=False)
        except Exception as e:
            raise Exception(f"Failed to click 'View Role' button")