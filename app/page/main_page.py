from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.contact_list_page import ContactList


class MainPage(BasePage):
    def goto_contact_menu_page(self):

        # 首页，点击通讯录进入通讯录列表界面
        self.driver.find_element(MobileBy.XPATH,'//*[@test="通讯录"]').click()
        return ContactList