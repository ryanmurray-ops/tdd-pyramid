# Automate Coin Duty Manager
 
## Project Overview
 
This project was completed over two phases using a Test Driven Development (TDD) approach.
 
The aim of the project was to build a system capable of managing Coins and Duties, starting with a simple web application before extending it into a fully tested REST API backed by a relational database.
 
---
 
# Phase 1
 
Phase 1 focused on building a basic Flask application to understand TDD and the different layers of an application.
 
Users could:
 
- Create Duties
- Validate user input
- Prevent duplicate Duty numbers
- Display created Duties on the page
 
At this stage, Duties were stored in memory rather than a database.
 
## Technologies
 
- Python
- Flask
- HTML
- Pytest
- Playwright
 
## Testing
 
Phase 1 introduced the TDD workflow by writing tests before implementation.
 
Tests included:
 
- Unit Tests
- Integration Tests
- End-to-End Tests using Playwright
 
Coverage exceeded the required 80%.
 
---
 
# Phase 2
 
Phase 2 extended the project into a REST API with persistent storage.
 
The application now stores Coins and Duties in a PostgreSQL database using Peewee ORM.
 
Coins can now:
 
- Be created
- Be updated
- Be deleted
- Be marked as complete
- Be retrieved by ID
- Be retrieved as a collection
- Be linked to one or more Duties
 
Duties can:
 
- Be created
- Be updated
- Be retrieved individually
- Be retrieved as a collection
 
Validation was added to ensure:
 
- Coin names remain unique
- Duty numbers remain unique
- Coins cannot be created without at least one valid Duty
- Duplicate duty assignments are prevented
- Only duty descriptions may be updated
 
---
 
# Technology Stack
 
- Python
- Flask
- PostgreSQL
- Peewee ORM
- Pytest
- AWS EC2
- GitHub
- GitHub Actions
 
---
 
# API Endpoints
 
## Coins
 
|  Method  |      Endpoint               |     Description             |
|----------|-----------------------------|-----------------------------|
|  GET     |      /coins                 |     Get all coins           |
|  GET     |      /coins/{id}            |     Get a coin by ID        |
|  POST    |      /coins                 |     Create a coin           |
|  PUT     |      /coins/{id}            |     Update a coin           |
|  DELETE  |      /coins/{id}            |     Delete a coin           |
|  PATCH   |      /coins/{id}/complete   |     Mark coin as complete   |
 
## Duties
 
|  Method  |      Endpoint               |     Description             |
|----------|-----------------------------|-----------------------------|
|  GET     |      /duties                |     Get all duties          |
|  GET     |      /duties/{number}       |     Get a duty              |
|  POST    |      /duties                |     Create a duty           |
|  PUT     |      /duties/{number}       |     Update a duty           |
 
---
 
# Testing
 
The project follows the Test Pyramid.
 
## Unit Tests
 
The majority of tests focus on business logic including:
 
- Coin Service
- Duty Service
- Models
- Relationships
 
## Integration Tests
 
Integration tests verify that the API routes interact correctly with the service layer and database.
 
These tests check:
 
- Status codes
- Validation
- Error handling
- JSON responses
 
## End-to-End Tests
 
Playwright was used during Phase 1 to test the original web interface.
 
---
 
# TDD Approach
 
The project was built using Test Driven Development.
 
For each new feature I generally followed this process:
 
1. Write a failing test.
2. Implement the smallest amount of code required to pass.
3. Refactor where appropriate.
4. Repeat.
 
This helped me build the project in small, testable pieces while giving me confidence that existing functionality continued to work.
 
---
 
# Deployment
 
The API is deployed to an AWS EC2 instance.
 
Deployment is automated using a GitHub Actions pipeline.
 
Whenever changes are pushed to the repository, the pipeline deploys the latest version to the EC2 server.
 
---
 
# Running the Project
 
## Install dependencies
 
pip install -r requirements.txt

 
## Start the application
 
python app.py

 
## Run the tests
 
pytest

 
## Generate coverage
 
pytest --cov=. --cov-report=term-missing
 
---
 
# Reflection
 
This project helped improve in several areas including:
 
- Test Driven Development
- REST APIs
- Database relationships
- Validation
- Git workflows
- CI/CD pipelines
- AWS deployment
 
Compared to Phase 1, I found Phase 2 much more challenging because changes in one area often affected multiple layers of the application. Following TDD made these changes much easier to manage because the existing tests quickly highlighted anything I had broken.
 
---
 
# Future Improvements
 
Given more time, there are several improvements I would make.
 
- Remove the remaining Phase 1 in-memory implementation so the application only uses the API and database.
- Refactor some of the test setup to reduce repeated code by introducing shared fixtures.
- Introduce controllers for both Coins and Duties to move business logic out of app.py and better separate responsibilities.
- Improve the front end so it utilises the REST API rather than using the original Phase 1 implementation.
- Remove remaining legacy code from Phase 1 that is no longer required.
 
Although these improvements would make the project cleaner and easier to maintain, I prioritised completing the required functionality and meeting the assignment criteria within the available time.