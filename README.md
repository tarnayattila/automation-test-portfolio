## Test Automation Framework (Selenium + Pytest + POM + Allure) 

![CI](https://github.com/tarnayattila/automation-test-portfolio/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-automation-green.svg)
![Pytest](https://img.shields.io/badge/pytest-testing-yellow.svg)
![POM](https://img.shields.io/badge/architecture-page%20object%20model-blueviolet.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black.svg)

A UI automation framework built with Selenium and Pytest using Page Object Model architecture.

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


pages/ – Page Object Model classes  
tests/ – Test cases (UI & regression)  
utils/ – helpers and utilities  
conftest.py – pytest fixtures  


---

## ▶️ Setup & Installation

### 1. Clone the repository

git clone https://github.com/tarnayattila/automation-test-portfolio.git
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