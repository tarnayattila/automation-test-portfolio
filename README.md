![Tests](https://github.com/user/repo/actions/workflows/tests.yml/badge.svg)
## Test Automation Framework (Selenium + Pytest + POM + Allure) 

## Overview

This is a **UI + api test automation framework** built with Python, Selenium and Pytest.

It demonstrates real-world Automation skills including:
- Page Object Model (POM) architecture
- UI functional testing
- Api testing
- Regression test suite
- Explicit waits for stability
- Allure reporting integration

The project simulates testing a real e-commerce web application.

---

## 🛠️ Tech Stack

- Python 3.x  
- Selenium WebDriver  
- Pytest  
- Page Object Model (POM)  
- Allure Reports  
- Git / GitHub  

---

## 📁 Project Structure


pages/ → Page Object Models
tests/ → Test cases
conftest.py → Fixtures & setup
requirements.txt
pytest.ini
allure-results/
allure-report/


---

## ▶️ Setup & Installation

### 1. Clone the repository

git clone https://github.com/tarnayattila/automation-framework.git
cd automation-framework


### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate


### 3. Install dependencies

pip install -r requirements.txt


---

##  Running Tests

### Run all tests:

pytest


---

##  Allure Report

### Generate results:

pytest --alluredir=allure-results


### Open report:

allure serve allure-results


---

## Framework Features

- Page Object Model architecture
- Reusable test components
- Clean separation of test layers
- Stable UI automation with explicit waits
- Scalable structure for CI/CD integration

---

##  Example Test Flow

Login Test:
1. Open login page  
2. Enter valid credentials  
3. Click login button  
4. Verify successful login  
5. Assert inventory page is displayed  

---

##  Future Improvements

- GitHub Actions CI pipeline  
- Cross-browser testing  
- Docker integration  
- API testing layer  

---

## Author

Attila Tarnay  
Automation Engineer

---

## ⭐ Purpose

This project was built to demonstrate:
- Real-world Automation skills  
- Selenium + Pytest framework design  
- Clean and scalable test architecture  
- Reporting with Allure  

---