import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage, log
from Pages.ProductsScreen import ProductsScreen
from Utilities import configReader
from Utilities.scroll_util import ScrollUtil


class LoginScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, flag, username, password, prodtitle, errorTxt):
        self.type("username_ACCESSIBILITYID", username)
        self.type("password_ACCESSIBILITYID", password)
        self.click("loginbtn_ACCESSIBILITYID")
        print(flag)
        match flag:
            case "vl":
                self.validateTitle(prodtitle)
                return ProductsScreen(self.driver)
            case "invl":
                self.validateErrorText(errorTxt)
            case default_case:
                print("something wrong")

    def validateErrorText(self, errorTxt):
        actual_err_txt = self.getText("errormsg_XPATH")
        expected_err_text = errorTxt
        assert expected_err_text == actual_err_txt, " Error texts are not matching"
        log.logger.error("Login is unsuccessful and the error message is-: " + str(actual_err_txt))

    def validateTitle(self, prodtitle):
        time.sleep(5)
        actual_text = self.getText("productstext_XPATH")
        expected_text = prodtitle
        assert expected_text == actual_text, " Titles are not matching"
        log.logger.info("Login is successful and the Product Screen title appears-: " + str(actual_text))
