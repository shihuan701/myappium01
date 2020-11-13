import pytest
import yaml

from app_blacklist.page.app import App


class TestContact():
    def setup_method(self):
        self.app = App()
        self.mainpage = self.app.start().goto_main()

    def teardown_method(self):
        self.app.stop()


    def test_contactadd(self):
        self.mainpage.goto_market_page().goto_search_page().search()
