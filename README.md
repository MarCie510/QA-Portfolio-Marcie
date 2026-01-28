# QA Engineering Portfolio - Marcie Jimenez

This repository contains a comprehensive suite of manual and automated testing projects, showcasing end-to-end quality assurance capabilities, from API logic to UI automation.

## 🚀 Project Structure

### 01-Test-Management
* **Tools:** Qase.io.
* **Content:** Professional Test Plans, Strategy documents, and Execution Reports.

### 02-API-Testing-Postman
* **Tools:** Postman (REST & SOAP/XML), JavaScript.
* **Content:**
    1.  **Booking API:** Management Suite with automated assertions.
    2.  **Trello API:** Workflow automation and Chaining (Dynamic Variables).
    3.  **ParaBank System:** Financial transaction tests dealing with Legacy XML responses.
* **Key Features:** Environment Variables management (`.json` included), Negative Testing, and Dynamic Data generation.

### 03-Web-UI-Testing
* **Framework:** Playwright + Python + Pytest.
* **Coverage:** Happy Path (Sign Up/Login) and Edge Cases (Negative testing).
* **Key Features:** Robust Selectors, Page Object Model (POM) pattern, and Google Ad-bypass logic.

## 🛠 Tools & Technologies

* **Automation:** Playwright, Python, Pytest, Selenium.
* **API Testing:** Postman, REST, JSON, XML.
* **Test Management:** Qase.io.
* **Environment:** macOS / Windows.
* **Version Control:** Git & GitHub.

## 📖 How to Run

### Web Tests (Python)
1.  Ensure you have the virtual environment active: `source venv/bin/activate`
2.  Run all tests: `pytest tests/`

### API Tests (Postman)
1.  Import the **Collection** (`.json`) and the **Environment** (`.json`) files into Postman.
2.  Select the imported Environment in the top-right corner.
3.  Run the collection via "Run Collection" runner.