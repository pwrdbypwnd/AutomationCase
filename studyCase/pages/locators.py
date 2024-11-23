from selenium.webdriver.common.by import By

class HomePageLocators:
    LOGO = (By.XPATH, "//img[@alt='insider_logo']")
    COMPANY_MENU = (By.XPATH, "//a[text()='Company']")
    CAREERS_MENU = (By.XPATH, "//a[text()='Careers']")

class CareersPageLocators:
    LOCATIONS_BLOCK = (By.XPATH, "//h2[text()='Locations']")
    TEAMS_BLOCK = (By.XPATH, "//h2[text()='Teams']")
    LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//h2[text()='Life at Insider']")
    SEE_ALL_QA_JOBS = (By.XPATH, "//a[text()='See all QA jobs']")
    LOCATION_FILTER = (By.NAME, "location")
    DEPARTMENT_FILTER = (By.NAME, "department")
    JOB_ITEM = (By.XPATH, "//div[@class='job-item']")
    POSITION = (By.XPATH, ".//h3")
    DEPARTMENT = (By.XPATH, ".//span[text()='Department']")
    LOCATION = (By.XPATH, ".//span[text()='Location']")
    VIEW_ROLE = (By.XPATH, "//a[text()='View Role']")
