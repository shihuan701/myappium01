from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.contact_menu_page import ContactMenu


class ContactList(BasePage):
    def goto_ContactMenu(self):
        # 滚动查找 添加成员 元素，并点击后进入添加成员菜单页面
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).\
                                 scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return ContactMenu