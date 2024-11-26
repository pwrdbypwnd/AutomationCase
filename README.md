# **📌 Insider Automation**

Welcome to the **Insider Automation Project**!  
This project automates UI testing and n11-Load Test for the **Insider** careers website using **Python**, **Selenium**, **locust** and **unittest**. Designed for efficiency, it organizes tests with structured execution, including screenshots for success and failure scenarios.

---

## **📋 Features**

- **UI Tests:**
  - Verify homepage logo visibility
  - Validate the page title correctness
  - Automate dropdown interactions (e.g., location and department filters)
  - Verify "View Role" button links
- **Dynamic Dropdown Selection:**
  - Adaptable to dynamic IDs and text-based selection
- **Screenshot Management:**
  - Automatic saving of success/failure screenshots
  - Organized in `ScreenShot/Success` and `ScreenShot/Fail`
- **Session Management:**
  - Single browser session for all tests
- **Configuration:**
  - Browser and test setup configurable via `.env`

---

## **🗂️ Project Structure**

```plaintext
InsiderAutomation/
│
├── .env                # Environment variables
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
│
├── studyCase/
│   ├── locust/         #n11 load test
│   ├── helpers/
│   │   └── utils.py    # Utility functions 
│   │
│   ├── pages/
│   │   ├── base.py       # Base class for common WebDriver operations
│   │   ├── careers_page.py  # Actions specific to the Careers page
│   │   ├── home_page.py     # Actions specific to the Home page
│   │   └── locators.py      # Centralized element locators
│
├── ScreenShot/
│   ├── Fail/           # Failed test screenshots
│   └── Success/        # Successful test screenshots
│
├── driver.py           # WebDriver initialization
├── mainTest.py         # Test cases using unittest
│
└── .gitignore          # Ignore files for Git



📦 Setup
1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Configure .env File

BROWSER=chrome

3️⃣ Run Tests

UI :
python mainTest.py

Load Test :
locust -f load_test.py --host=https://www.n11.com


🛠 Workflow

Test Execution Steps:

Initialize WebDriver

Perform UI tests:
Verify homepage logo and title
Navigate to Careers and interact with dropdowns
Verify "View Role" links


Take and save screenshots:

Success: ScreenShot/Success
Failure: ScreenShot/Fail
End the browser session

📑 Test Scenarios

Homepage Tests:

Verify logo visibility using alt='insider_logo'
Check title matches Ready to disrupt? | Insider Careers
Dropdown Interaction:

Open location dropdown and select "Istanbul, Turkey"
Ensure department dropdown defaults to "Quality Assurance" or select it

View Role Validation:

Verify "View Role" button links match expected URLs
Open and validate URLs in new tabs

📸 Screenshot Examples

ScreenShot/
├── Success/
│   └── test_home_page_logo_2024-11-26.png
└── Fail/
    └── test_dropdown_interaction_2024-11-26.png
🔮 Future Plans

Add API tests for Swagger endpoints
Integrate Allure for test reporting
Introduce CI/CD pipelines for automated testing
Expand to include performance and load testing tools like Locust or JMeter

💡 Why This Project?
This project streamlines QA processes with structured tests, configurable setups, and detailed results, enabling effective test automation for dynamic web applications. """

