from appium import webdriver

from app.page.main_page import MainPage


class TestContact():
    def setup_method(self):
        self.mainpage = MainPage()

    def teardown_method(self):
        self.mainpage.stop()

    def test_contactadd(self):
        name = "sw0040"
        gender = "男"
        phonenum = "17777777740"
        toast_text = self.mainpage.goto_contact_menu_page() \
            .goto_ContactMenu()\
            .goto_ContactAdd()\
            .add(name, gender, phonenum).get_toast()
        assert '添加成功' == toast_text


    def test_contactedit(self):
        name = "sw0040"
        isExist = self.mainpage.goto_contact_menu_page() \
            .goto_ContactEditlist_page()\
            .goto_ContactEdit(name)\
            .delete().checkuser(name)
        assert isExist == False