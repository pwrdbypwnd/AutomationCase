from selenium.webdriver.common.by import By

class HomePageLocators:
    LOGO = (By.CSS_SELECTOR, "img[alt='insider_logo']")
    COMPANY_XPATH = (
    By.XPATH, "//ul[@class='navbar-nav']//a[@id='navbarDropdownMenuLink' and contains(text(), 'Company')]")
    CAREERS_XPATH = (
    By.XPATH, "//div[contains(@class, 'dropdown-menu new-menu-dropdown-layout-6')]//a[text()='Careers']")

class CareersPageLocators:

    EXPAND_BUTTON_XPATH = "//a[contains(@class, 'loadmore') and normalize-space(text())='See all teams']"
    QUALITY_ASSURANCE_XPATH = "(//div//a[contains(@href, 'quality-assurance')])[1]"
    SEE_ALL_QA_JOBS_XPATH = "//a[@class='btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50' and contains(text(), 'See all QA jobs')]"
    FILTER_LOCATION_BY_ID = "select2-filter-by-location-container"
    FILTER_DEPARTMENT_BY_ID = "select2-filter-by-department-container"
    SELECT_LOCATION_BY_XPATH = "//li[contains(@class, 'select2-results__option') and text()='{option_text}']"
    SELECT_DEPARTMENT_BY_XPATH = "//li[contains(@class, 'select2-results__option') and text()='{option_text}']"
    RESULT_COUNTER_ID = "deneme"
    VIEW_ROLE_BUTTON = "//a[contains(@class, 'btn-navy') and text()='View Role']"