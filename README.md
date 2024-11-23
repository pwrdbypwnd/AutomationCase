
# **📌 Insider Automation**

Welcome to the **Insider Automation Project**!  
This project is designed to automate UI and API testing for the **Insider** website. Built with **Python** and **Selenium**, the tests are executed using the `unittest` framework, capturing screenshots for both **success** and **failure** scenarios.

---

## **📋 Features**

```plaintext
============================================================
🎯 UI Tests
    ✔ Validate the homepage logo visibility.
    ✔ Verify the correctness of the page title.
============================================================
📸 Screenshot Management
    ✔ Screenshots for both success and failure scenarios.
    ✔ Organized into separate folders: `Success` and `Failure`.
============================================================
🛠 Single Browser Session
    ✔ All tests run within a single browser session.
============================================================
⚙️ Easy Configuration
    ✔ Browser selection via `.env` file.
============================================================
```

---

## **🗂️ Project Structure**

```plaintext
InsiderAutomation/
│
├── pages/
│   ├── base_page.py          # Base class for common page operations
│   ├── home_page.py          # Handles operations for the homepage
│   ├── careers_page.py       # Handles operations for the careers page
├── tests/
│   ├── test_insider.py       # Contains test scenarios
├── helpers/
│   ├── utils.py              # Helper functions (e.g., taking screenshots)
├── driver.py                 # WebDriver initialization and management
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables (e.g., browser selection)
├── README.md                 # Project documentation


```

---

## **📦 Setup**

### **1️⃣ Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **2️⃣ Configure `.env` File**
Create a `.env` file in the root directory and specify the browser:
```plaintext
BROWSER=chrome
```

### **3️⃣ Run the Tests**
Execute the test suite:
```bash
python test_insider.py
```

---

## **🛠 Workflow**

```plaintext
1️⃣ Initialize WebDriver
2️⃣ Perform UI tests:
   - Check homepage logo visibility.
   - Verify page title correctness.
3️⃣ Take screenshots:
   - Success: Saved in `ScreenShot/Success`.
   - Failure: Saved in `ScreenShot/Failure`.
4️⃣ Close browser session after all tests.
```

---

## **📑 Test Scenarios**

### **✅ Homepage Logo Test**
- **Objective:** Verify the visibility of the homepage logo.
- **Locator:** `//img[@alt='insider_logo']`

### **✅ Homepage Title Test**
- **Objective:** Validate the title of the homepage.
- **Expected Title:** `#1 Leader in Individualized, Cross-Channel CX — Insider`

---

## **📸 Screenshot Organization**

```plaintext
ScreenShot/
├── Success/
│   ├── test_home_page_logo_2024-11-21_15-00-00.png
│   ├── test_home_page_title_2024-11-21_15-02-00.png
│
├── Failure/
    ├── test_home_page_logo_2024-11-21_15-01-00.png
    ├── test_home_page_title_2024-11-21_15-03-00.png
```

---

## **📚 Example Output**

| Test Case                | Result  | Screenshot Location        |
|--------------------------|---------|----------------------------|
| Homepage Logo Visibility | ✅ Success | `ScreenShot/Success/test_home_page_logo_2024-11-21_15-00-00.png` |
| Homepage Title Check     | ❌ Failure | `ScreenShot/Failure/test_home_page_title_2024-11-21_15-03-00.png` |


---

## **🔮 Future Enhancements**

### 🔧 Planned Features
- **API Tests:**
  - CRUD operations for Swagger PetStore.
  - Positive and negative test scenarios.
- **Load Testing:**
  - Using JMeter or Locust for performance evaluation.
- **Reporting:**
  - Integrate Allure for detailed test reports.

---

## **🔗 Contribution Guidelines**

We welcome contributions! Follow these steps:

1. **Fork the repository.**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes:**
   ```bash
   git commit -m "Add your feature description here."
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a pull request!**

---

## **📜 License**
This project is open-source and free to use. Use at your own discretion.

---

## **📂 Project Schema**

```plaintext
    ┌────────────────────────────────────────┐
    │          Insider Automation           │
    └────────────────────────────────────────┘
                  ▲             ▲
                  │             │
    ┌────────────┴─────────────┴────────────┐
    │                                       │
┌───────────┐                      ┌────────────────┐
│ Driver.py │                      │  Pages.py      │
└───────────┘                      └────────────────┘
      ▲                                  ▲
      │                                  │
┌──────────────┐                  ┌──────────────────┐
│ Test Suite   │ <──────────────> │ Helpers (Utils)  │
└──────────────┘                  └──────────────────┘
```

---

## **💡 Why This Project?**
This project simplifies automated testing for web applications. With structured tests, configurable settings, and detailed results, it ensures both clarity and efficiency in QA workflows.
