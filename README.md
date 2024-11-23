# InsiderAutomation

**Study Cases - Insider UI and API Test Automation**


**-------------------------Setup---------------------------**
**Python Installation** 
3.13 Latest version of python : 
https://www.python.org/downloads/ 
**----------------------------------------------------**
**Install Dependencies**
pip install -r requirements.txt
**----------------------------------------------------**
**Configure .env File**
#Supports Chrome and Firefox WebDrivers for now
#OPTION1=chrome , OPTION2=firefox 
BROWSER=chrome
**----------------------------------------------------**
**Run the Tests**
#path/to/your/location
python unitTest.py

**================================ Workflow ====================================================**
1️ Initialize WebDriver
2️ Perform UI tests:
   - Check homepage logo visibility.
   - Verify page title correctness.
3️ Take screenshots:
   - Success: Saved in `ScreenShot/Success`.
   - Failure: Saved in `ScreenShot/Failure`.
4️ Close browser session after all tests.



**================================ Project Structure ============================================**
InsiderUIandApiTest/
│
├── driver.py           # WebDriver initialization and browser management.
├── pages.py            # Page actions and interactions.
├── helpers.py          # Helper functions for screenshot handling and more.
├── test_insider.py     # Test cases for UI validation.
├── ScreenShot/         # Screenshots folder (organized into `Success` and `Failure`).
├── .env                # Environment variables (e.g., browser selection).
├── .gitignore          # Files and folders to exclude from Git.
├── requirements.txt    # Python dependencies.
├── README.md           # Project documentation (this file).



**================================ Features =====================================================**
  - UI Tests
     *Validate the homepage logo visibility.
     *Verify the correctness of the page title.
**============================================================**
  - Screenshot Management
     *Screenshots for both success and failure scenarios.
     *Organized into separate folders: `Success` and `Failure`.
**============================================================**
  - Single Browser Session
     *All tests run within a single browser session.
**============================================================**
⚙️ Easy Configuration
    ✔ Browser selection via `.env` file.
============================================================


