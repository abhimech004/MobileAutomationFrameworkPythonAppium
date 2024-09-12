import pytest

from Pages.AddToCartScreen import AddToCartScreen
from Pages.CheckoutScreen import CheckoutScreen
from Pages.LoginScreen import LoginScreen
from Pages.ProductsScreen import ProductsScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_AddToCart(BaseTest):

    @pytest.mark.parametrize("flag,username,password,prodtitle,errorTxt,product,fname,lname,zipcode,confirmText", dataProvider.get_data("AddToCartData"))
    def test_add_to_cart(self, flag, username, password, prodtitle, errorTxt, product, fname, lname, zipcode, confirmText):
        login = LoginScreen(self.driver)
        login.do_login(flag, username, password, prodtitle, errorTxt).add_to_cart(product).click_checkout_btn().addcustomerDetails(fname, lname, zipcode, confirmText)


        
