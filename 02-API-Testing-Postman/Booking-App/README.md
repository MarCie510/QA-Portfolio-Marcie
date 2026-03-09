{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Booking API - Technical Documentation\
\
## \uc0\u55357 \u56541  Testing Strategy & Rationale\
This project applies professional QA standards to ensure the resilience of the Restful Booker API:\
\
* **Equivalence Partitioning:** Used to categorize requests into valid and invalid sets, ensuring the API returns correct status codes (200 OK vs. 400/500 Error).\
* **Negative Testing:** Validated how the API handles missing mandatory fields (e.g., firstname) to ensure robust error handling and server stability.\
* **Risk-Based Testing (MoT approach):** Priority was given to Authentication and the CRUD cycle (Create, Read, Update, Delete) as they are the core business processes.\
* **Contract Testing:** Applied JSON Schema validation to ensure the API response structure remains consistent.\
\
## \uc0\u9881 \u65039  Key Automation Features\
* **Dynamic Chaining:** Automated token generation and ID passing between requests.\
* **Data Sanitization:** Implemented environment teardown to clear variables after test execution.\
* **Test Coverage:** Includes both Happy Path and Edge Cases with descriptive English assertions.}