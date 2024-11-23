import os
from selenium import webdriver
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DriverHelper:
    @staticmethod
    def get_driver():
        # Read browser choice from .env file
        browser = os.getenv("BROWSER", "chrome").lower()

        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # Maximize browser window and set implicit wait
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
