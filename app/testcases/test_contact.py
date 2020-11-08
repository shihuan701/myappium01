import pytest
import yaml

from app.page.app import App


class TestContact():
    def setup_method(self):
        self.app = App()
        self.mainpage = self.app.start().goto_main()

    def teardown_method(self):
        self.app.stop()



    @pytest.mark.parametrize('name,gender,phonenum',[('sw0040','女','17777777740')])
    def test_contactadd(self,name,gender,phonenum):
        toast_text = self.mainpage.goto_contact_menu_page() \
            .goto_ContactMenu()\
            .goto_ContactAdd()\
            .add(name, gender, phonenum).get_toast()
        assert '添加成功' == toast_text


    @pytest.mark.parametrize('name', [('sw0040')])
    def test_contactedit(self,name):
        isExist = self.mainpage.goto_contact_menu_page() \
            .goto_ContactEditlist_page()\
            .goto_ContactEdit(name)\
            .delete().checkuser(name)
        assert isExist == False

