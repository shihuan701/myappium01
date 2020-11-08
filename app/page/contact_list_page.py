from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage



class ContactList(BasePage):
    def goto_ContactMenu(self):
        # 滚动查找 添加成员 元素，并点击后进入添加成员菜单页面
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        from app.page.contact_menu_page import ContactMenu
        return ContactMenu(self.driver)

    def goto_ContactEditlist_page(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="石一科技"]/../../../../../android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]').click()
        from app.page.contact_preedit_page import PreContactEdit
        return PreContactEdit(self.driver)