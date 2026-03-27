# QA Engineering Portfolio — Marcie Jimenez

End-to-end quality assurance portfolio covering manual testing, API automation, and UI automation, built following ISTQB and Ministry of Testing (MoT) standards.

![Playwright Tests](https://github.com/MarCie510/QA-Portfolio-Marcie/actions/workflows/playwright.yml/badge.svg)

---

## Project Structure

### [01 — Test Management](./01-Test-Management)
- **Tools:** Qase.io
- **Content:** Test Plans, Strategy documents, and Execution Reports following professional QA standards

### [02 — API Testing (Postman)](./02-API-Testing-Postman)
- **Tools:** Postman (REST & SOAP/XML), JavaScript
- **Projects:**
  1. [**Booking API — Management Suite**](./02-API-Testing-Postman/Booking-App): Full CRUD cycle with JSON Schema validation, Edge Cases, and environment teardown following ISTQB & MoT standards
  2. [**Trello API**](./02-API-Testing-Postman/Trello-Framework): Workflow automation with Dynamic Variables and request chaining
  3. [**ParaBank System**](./02-API-Testing-Postman/ParaBank-System): Financial transaction tests handling Legacy XML/SOAP responses
- **Key Features:** Environment Variables, Positive/Negative Testing, Dynamic Data generation, automated Teardown

### [03 — Web UI Automation](./03-Web-UI-Testing)
- **Framework:** Playwright + Python + Pytest
- **Pattern:** Page Object Model (POM)
- **Coverage:**
  - ✅ Happy Path — successful login flow
  - ✅ Negative Testing — invalid credentials handling
  - 🔜 Edge Cases — boundary inputs, timeouts, session handling *(planned)*
- **CI/CD:** Automated via GitHub Actions on every push

---

## Tools & Technologies

| Area | Tools |
|---|---|
| UI Automation | Playwright, Python, Pytest |
| API Testing | Postman, REST, JSON, XML/SOAP |
| Test Management | Qase.io |
| CI/CD | GitHub Actions |
| Version Control | Git & GitHub |

---

## How to Run

### Web Tests (Python)
```bash
cd 03-Web-UI-Testing
source venv/bin/activate
pytest tests/
```

### API Tests (Postman)
1. Import the **Collection** and **Environment** `.json` files into Postman
2. Select the imported environment from the top-right dropdown
3. Click **Run Collection** to execute all requests