import os
from pathlib import Path
import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    report_path = str(Path().absolute().parent) + "\\TestCases\\testreports.html"
    delete_existing_report(report_path)
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

    desired_caps = {
        "deviceName": "Android",
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": "com.swaglabsmobileapp.SplashActivity",
        "app": str(Path().absolute().parent) + "\\app\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
    }
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    appium_service.stop()

def delete_existing_report(report_path):
    if os.path.exists(report_path):
        os.remove(report_path)
        print(f"Deleted existing report: {report_path}")
    else:
        print("No existing report found.")

# @pytest.fixture(params=['device1', 'device2'], scope="function")
# def appium_driver(request):
#
#     if request.param == 'device1':
#         desired_cap = dict(
#             deviceName='Android',
#             platformName='Android',
#             udid='892722a8',
#             appPackage='com.swaglabsmobileapp',
#             appActivity='com.swaglabsmobileapp.SplashActivity',
#             automationName='UiAutomator2',
#             app=str(Path().absolute().parent) + "\\app\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
#         )
#         capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)
#         driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
#         request.cls.driver = driver
#
#     if request.param == 'device2':
#         desired_cap = dict(
#             deviceName='Android',
#             platformName='Android',
#             udid='emulator-5554',
#             appPackage='com.swaglabsmobileapp',
#             appActivity='com.swaglabsmobileapp.SplashActivity',
#             automationName='UiAutomator2',
#             app=str(Path().absolute().parent) + "\\app\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
#         )
#         capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)
#         driver = webdriver.Remote('http://127.0.0.1:4724', options=capabilities_options)
#         request.cls.driver = driver
#
#     driver.implicitly_wait(10)
#     yield driver
#     time.sleep(3)
#     driver.quit()

@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
