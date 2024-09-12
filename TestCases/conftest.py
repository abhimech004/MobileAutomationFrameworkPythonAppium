from pathlib import Path

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options


#test case failure status
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# @pytest.fixture(scope="function")
# def appium_driver(request):
#     desired_caps = {
#         'platformName': 'Android',
#         'deviceName': 'Android',
#         'appPackage': 'com.goibibo',
#         'appActivity': '.common.HomeActivity',
#         'app': str(Path().absolute().parent) + "\\app\\Goibibo.apk"
#     }
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     request.cls.driver = driver
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

@pytest.fixture(scope="function")
def appium_driver(request):
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


#capturing screenshot in case of failure
@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
