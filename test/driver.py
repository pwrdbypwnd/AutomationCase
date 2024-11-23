import os
from selenium import webdriver
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

class DriverHelper:
    @staticmethod
    def get_driver():
        """
        .env dosyasından tarayıcı seçimini okur ve WebDriver başlatır.
        """
        browser = os.getenv("BROWSER", "chrome")  # Varsayılan olarak Chrome
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"{browser} tarayıcısı desteklenmiyor!")

        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
