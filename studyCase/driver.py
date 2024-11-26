import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Load environment variables from .env file
load_dotenv()


class DriverHelper:
    @staticmethod
    def get_driver(enable_zoom=False, zoom_factor=1.75):
        # Read browser choice from .env file
        browser = os.getenv("BROWSER", "chrome").lower()

        if browser == "chrome":
            options = ChromeOptions()
            # Add zoom option if enabled
            if enable_zoom:
                options.add_argument(f"--force-device-scale-factor={zoom_factor}")
            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            # Add zoom option if enabled
            if enable_zoom:
                options.set_preference("layout.css.devPixelsPerPx", str(zoom_factor))
            driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # Maximize browser window
        driver.maximize_window()
        return driver
