# Automate Coin Duty Manager
 
## Project Overview
 
This is a Flask web application that allows users to create and manage duties linked to the Automate Coin.
 
Users are able to:
- Add a duty using a form
- View all created duties on the homepage
- Ensure duty numbers are unique
- See error messages when invalid input is submitted
 
This project was built using Test Driven Development (TDD), where tests were written first and the implementation was built to satisfy them.
 
---
 
## Tech Stack
 
This project uses:
 
- Python
- Flask (web framework)
- HTML for the front-end
- Pytest for unit and integration testing
- Playwright for end-to-end testing
- unittest.mock for mocking in integration tests
 
---
 
## Features
 
### Duty Management
Users can add duties using a simple form.
 
Once submitted, the duty is displayed in a list on the page.
 
### Validation Rules
- Duty number must not be empty
- Duty description must not be empty
- Duty numbers must be unique
 
### Error Handling
If invalid data is submitted, an error message is displayed and the duty is not added.
 
---
 
## Testing
 
The project follows a basic test pyramid structure.
 
### Unit Tests
Unit tests focus on testing individual functions in isolation.
 
They cover:
- Duty creation logic
- Input validation
- Duplicate duty checks
 
---
 
### Integration Tests
Integration tests check how the Flask application works with the rest of the system.
 
They:
- Send requests to Flask routes
- Check responses from the server
- Verify duties are created correctly through the web layer
- Use mocking where needed to isolate behaviour
 
---
 
### End-to-End Tests
End-to-end tests use Playwright to simulate real user interaction in a browser.
 
They verify:
- The homepage loads correctly
- Duties can be added through the form
- Duties appear on the page
- Error messages are shown when expected
 
---

### Mocking

In some of my integration tests I used mocking to isolate parts of the app that were not relevant to the specific test being run.

For example, I mocked the handle_create_duty function when testing the route. This allowed me to test the route behaviour without relying in the actual business logic inside the function.

This helped me:
- Isolate the route from the business logic
- Ensure tests were focused on what the route returns
- Avoid unnecessary dependencies during testing

I used unittest.mock.patch to replace the function during the test.

This improved the test reliability and made the integratiin tests faster and more focused.

---

### Test Coverage Report

Coverage was generate using pytest-cov.

**Command Used**
pytest --cov=. --cov-report=term-missing

**Coverage Summary**
- Overall: 91%
- Total Statements: 220
- Missed Statements: 19

Most of the missed coverage is in the end-to-end tests, which is expected as they focus on full user flows rather than testing branch of code.

Most of the core business logic is covered by unit and integration tests, which is why modules such as duties.py, validators.py, and services/duty_service.py achieve 100% coverage.

---

## Test Pyramid Explanation

This project follows a basic test pyramid structure to ensure the application is well tested at different levels of scope.

## Unit Tests

Unit tests make up the majority of the test suite. They focus on testing individual functions in isolation, such as validation logic and duty creation.

## Integration Tests

Integration tests check how different parts of the application work toegther. In this project, they test the Flask routes and ensure that the layers interact correctly with the business logic.

## End-to-End Tests

End-to-End tests use Playwright to simulate real user behaviour in a browser. These tests ensure the full system works from the users perspective, including form submissions and UI updates.

## Test Distribution
The majority of tests are unit tests, with fewer integration and end-to-end tests. This is intentional because unit tests are faster and more focused, while high-level tests are used to validate overall system behaviour.

This approach helps balance test speed with reliability and overall coverage.

---
 
## How to Run the Project
 
### Install Dependencies
 
Before running the app, install the required packages:
 
- pip install flask pytest pytest-cov playwright
 
 
 
## How to Run the Project
 
### Install Dependencies
 
Before running the app, install the required packages:
 
- pip install flask pytest pytest-cov playwright
 
---
 
### Run the App
 
To start the Flask application:
 
python app.py
 
Then open:
 
http://localhost:5000
 
---
 
### Run Tests
 
To run all tests:
 
pytest
 
---
 
### Check Test Coverage
 
To generate a coverage report:
 
pytest --cov=. --cov-report=term-missing
 
The project currently has over 80% test coverage, which meets the requirement.
 
---
 
### End-to-End Tests
 
End-to-end tests use Playwright and run through real browser interactions.
 
To run them:
 
pytest
 
---
 
## Deployment
 
This project is deployed using AWS as part of a CI/CD pipeline.
 
When changes are pushed to the repository, the application is automatically built and deployed.