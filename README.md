# SauceDemo Selenium Automation Project (Python)
This project is a *Selenium + Python automation framework* built to test the functionality of the [SauceDemo](https://www.saucedemo.com/) web application.  
It covers basic **end-to-end UI test automation scenarios** such as login, product selection, cart operations, and checkout flow.

---
## Project Overview

The main goal of this project is to practice and demonstrate:
- Selenium Web Automation with Python
- Test case design and execution
- Page interactions (login, add to cart, checkout)
- Basic framework structure for QA automation

---
## Tech Stack

 Python
- Selenium WebDriver
- Pytest
- ChromeDriver
- Logging Module
- RotatingFileHandler
- Git & GitHub

  ---
## Logging Implementation

This framework includes a custom logging utility to capture test execution details.

### Logging Features:

- Generates execution logs automatically
- Supports both console and file logging
- Uses `RotatingFileHandler` to prevent log files from growing indefinitely
- Maintains previous log history using backup log files

```text
2026-07-13 12:30:10 | INFO | login_page.py | enter_username | Entering username
---
## Project Structure

```text
saucedemo_project
│
├── config
│   └── config.py
│
├── page_object
│   └── login_page.py
│
├── test
│   └── test_login.py
│
├── utilities
│   └── logger.py
│
├── logs
│   └── automation.log
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```
  
