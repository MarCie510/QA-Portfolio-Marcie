# SauceDemo E2E Testing Project

This project demonstrates a professional QA workflow, integrating manual test management with automated regression testing.

---

## 🏗️ Test Management with Qase.io
I designed a comprehensive test suite of **41 test cases** in Qase.io, ensuring 100% coverage of critical business flows.

* **Trazability:** Every automated test in this repository is mapped to its corresponding Manual Test Case ID (e.g., `SDW-10`).
* **Artifacts:** * Manual Test Cases: Available in `manual/` (XML/CSV).
    * Execution Reports: Professional PDF reports of manual and automated runs are located in `docs/`.
* **Strategy:** Includes Smoke Testing, Regression, and specialized Edge Case/Security validation.

## 📂 Project Structure
* **[automation/](./automation):** Playwright + Python framework following the Page Object Model (POM).
* **[docs/](./docs):** Contains the Master Test Plan, manual execution reports, and automation results.
* **[manual/](./manual):** Documentation of the 41 test cases designed for this project.

## 🛠️ Tech Stack
* **Test Management:** Qase.io (TCM)
* **Automation:** Playwright (Python)
* **Test Runner:** Pytest
* **Reporting:** Pytest-html & Qase Execution Reports

## 🚀 How to Run Automation
1.  **Activate Environment:** `source venv/bin/activate`
2.  **Run All Tests:** `python3 -m pytest`
3.  **Generate Report:** `python3 -m pytest --html=reports/regression_report.html --self-contained-html`

## 📊 Latest Results
* **Manual:** 100% Pass rate on Smoke Suite.
* **Automation:** 40 Passed, 1 Expected Failure (Known Bug SDW-25).
