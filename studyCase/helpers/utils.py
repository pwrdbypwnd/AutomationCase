import os
import datetime

def take_screenshot(driver, test_name, success=True):
    # Determine folder path based on test result
    status = "Success" if success else "Failure"
    folder_path = f"ScreenShot/{status}"
    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the screenshot with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(folder_path, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
