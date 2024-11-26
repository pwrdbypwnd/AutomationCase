import datetime
import os


def take_screenshot(driver, test_name, success=True):
    status = "Success" if success else "Fail"
    folder_path = f"ScreenShot/{status}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(folder_path, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
