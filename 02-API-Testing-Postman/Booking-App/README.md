# Booking API — Management Suite

Automated test suite for the [Restful Booker API](https://restful-booker.herokuapp.com/), built with Postman and JavaScript following ISTQB and Ministry of Testing (MoT) standards.

---

## Testing Strategy & Rationale

This project applies professional QA standards to validate the resilience and correctness of the API across its full CRUD lifecycle.

| Technique | Application |
|---|---|
| **Equivalence Partitioning** | Requests categorized into valid and invalid sets, verifying correct status codes (200 OK vs. 400/500 Error) |
| **Negative Testing** | Validated behavior when mandatory fields (e.g., `firstname`) are missing, ensuring robust error handling and server stability |
| **Risk-Based Testing (MoT)** | Priority given to Authentication and the full CRUD cycle — the core business processes |
| **Contract Testing** | JSON Schema validation applied to ensure API response structure remains consistent across runs |

---

## Key Automation Features

- **Dynamic Chaining** — Automated token generation and ID passing between requests, so no manual intervention is needed between test steps
- **Data Sanitization** — Environment teardown clears all variables after execution, ensuring a clean state for every run
- **Test Coverage** — Includes Happy Path and Edge Cases with descriptive English assertions

---

## Project Structure
```
Booking-App/
├── 01. Booking - Env.postman_environment.json
├── 01. Booking API - Management Suite.postman_collection.json
└── README.md
```

## How to Run

1. Open **Postman** and import both `.json` files (collection + environment)
2. Select the `Booking-API` environment from the top-right dropdown
3. Click **Run Collection** and execute all requests in order

> The collection handles authentication and teardown automatically — no manual setup required between runs.

---

## Test Coverage Summary

| Area | Type | Status |
|---|---|---|
| Authentication (token generation) | Happy Path + Negative | ✅ Covered |
| Create Booking (POST) | Happy Path + Edge Cases | ✅ Covered |
| Get Booking (GET) | Happy Path + Schema validation | ✅ Covered |
| Update Booking (PUT/PATCH) | Happy Path + Negative | ✅ Covered |
| Delete Booking (DELETE) | Happy Path + Teardown | ✅ Covered |
| Missing mandatory fields | Negative Testing | ✅ Covered |

---

## Tools & Standards

- **Postman** — REST collection runner with JavaScript test scripts
- **JSON Schema** — Contract validation on all response bodies
- **ISTQB** — Test design techniques (EP, BVA, Negative Testing)
- **MoT (Ministry of Testing)** — Risk-based prioritization approach