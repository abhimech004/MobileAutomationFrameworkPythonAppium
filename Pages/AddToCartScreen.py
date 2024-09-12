
from Pages.BasePage import BasePage, log
from Pages.CheckoutScreen import CheckoutScreen
from Utilities.scroll_util import ScrollUtil


class AddToCartScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout_btn(self):
        ScrollUtil.scrollToTextByAndroidUIAutomator("CHECKOUT", self.driver)
        self.click("checkoutbtn_XPATH")
        return CheckoutScreen(self.driver)


