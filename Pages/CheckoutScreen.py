import time
from Pages.BasePage import BasePage, log
from Utilities.scroll_util import ScrollUtil


class CheckoutScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def addcustomerDetails(self, fname, lname, zipcode, confirmText):
        self.click("firstname_XPATH")
        self.type("firstname_XPATH", fname)
        self.click("lastname_XPATH")
        self.type("lastname_XPATH", lname)
        self.click("zip_XPATH")
        self.type("zip_XPATH", zipcode)
        self.driver.hide_keyboard()
        time.sleep(2)
        self.click("continuebtn_XPATH")
        time.sleep(2)
        ScrollUtil.scrollToTextByAndroidUIAutomator("FINISH", self.driver)
        self.validateThanksTxt(confirmText)

    def validateThanksTxt(self, confirmText):
        time.sleep(5)
        actual_text = self.getText("thanktext_XPATH")
        expected_text = confirmText
        assert expected_text == actual_text, " Titles are not matching"
        log.logger.error("Order is completed-: " + str(actual_text))



