# SauceDemo - Master Test Plan 🚀

## 1. Introduction & Objectives
This project ensures the quality and reliability of the SauceDemo e-commerce platform. It integrates comprehensive manual testing results with a scalable UI automation framework.

## 2. Scope
* **In-Scope:** Authentication, Product Catalog, Shopping Cart, and Checkout flow.
* **Out-of-Scope:** Performance testing and actual Payment Gateway integration (mocked).

## 3. Test Levels & Types
* **Manual Testing:** Exploratory and regression testing (See `docs/Manual_Execution_Report.pdf`).
* **Automated Testing:** Regression suite for stable features using **Playwright + Python**.
* **Value-Based Testing:** Inclusion of positive and negative scenarios (happy path and edge cases).

## 4. Tools & Environment
* **Test Management:** [Qase.io](https://qase.io) (Internal Repository).
* **Automation Framework:** Playwright (Python).
* **CI/CD:** GitHub Actions.
* **Environment:** https://www.saucedemo.com/

## 5. Automation Strategy (POM)
We implement the **Page Object Model (POM)** pattern. Tests are data-driven to cover multiple user profiles (standard, locked_out, problem, etc.).

## 6. Definition of Done (DoD)
- [ ] 100% of planned manual cases executed.
- [ ] Critical path automated and passing in CI/CD.
- [ ] Documentation updated and Peer Reviewed.