from base_page import BasePage
from locators import CareersPageLocators

class CareersPage(BasePage):
    def verify_blocks_visibility(self):
        return (
            self.is_element_visible(*CareersPageLocators.LOCATIONS_BLOCK)
            and self.is_element_visible(*CareersPageLocators.TEAMS_BLOCK)
            and self.is_element_visible(*CareersPageLocators.LIFE_AT_INSIDER_BLOCK)
        )

    def filter_jobs(self, location, department):
        self.click_element(*CareersPageLocators.SEE_ALL_QA_JOBS)
        self.driver.find_element(*CareersPageLocators.LOCATION_FILTER).send_keys(location)
        self.driver.find_element(*CareersPageLocators.DEPARTMENT_FILTER).send_keys(department)

    def get_job_details(self):
        jobs = self.driver.find_elements(*CareersPageLocators.JOB_ITEM)
        job_details = []
        for job in jobs:
            position = job.find_element(*CareersPageLocators.POSITION).text
            department = job.find_element(*CareersPageLocators.DEPARTMENT).text
            location = job.find_element(*CareersPageLocators.LOCATION).text
            job_details.append((position, department, location))
        return job_details

    def view_role_and_verify_redirection(self):
        self.click_element(*CareersPageLocators.VIEW_ROLE)
        return "lever.co" in self.driver.current_url
