import allure
import pytest
from pip._internal.utils import datetime

from core.driver_factory import create_driver
import os
from datetime import datetime

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def pytest_configure(config):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        report_dir = os.path.join(base_dir, "", "reports")

        os.makedirs(report_dir, exist_ok=True)

        config.option.htmlpath = os.path.join(report_dir, "report.html")
        config.option.self_contained_html = True

def pytest_html_report_title(report):
        report.title = "Automation Test Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure",
                attachment_type=allure.attachment_type.PNG
            )