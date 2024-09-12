import time

from appium.webdriver.common.appiumby import AppiumBy
from Pages.AddToCartScreen import AddToCartScreen
from Pages.BasePage import BasePage
from Utilities import configReader
from Utilities.scroll_util import ScrollUtil


class ProductsScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self, product):
        ScrollUtil.scrollToTextByAndroidUIAutomator(product, self.driver)
        #ScrollUtil.scrollToTextByAndroidUIAutomator("Sauce Labs Onesie", self.driver)
        ScrollUtil.scrollToTextByAndroidUIAutomator("ADD TO CART", self.driver)
        time.sleep(5)
        self.click("testcarticon_XPATH")
        time.sleep(5)
        return AddToCartScreen(self.driver)




