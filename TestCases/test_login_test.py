import pytest

from Pages.LoginScreen import LoginScreen
from Pages.ProductsScreen import ProductsScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_LoginTest(BaseTest):

    @pytest.mark.parametrize("flag,username,password,prodtitle,errorTxt", dataProvider.get_data("LoginData"))
    def test_login(self, flag, username, password, prodtitle, errorTxt):
        login = LoginScreen(self.driver)
        login.do_login(flag, username, password, prodtitle, errorTxt)