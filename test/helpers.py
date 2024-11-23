import os
import datetime

def take_screenshot(driver, test_name, success=True):
    """
    Test sonucuna göre ekran görüntüsü alır.
    """
    status = "Success" if success else "Fail"
    screenshot_dir = os.path.join("ScreenShot", status)
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

    driver.save_screenshot(screenshot_path)
    print(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
