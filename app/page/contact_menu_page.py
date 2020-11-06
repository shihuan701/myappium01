from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.contact_add_page import ContactAdd


class ContactMenu(BasePage):
    def goto_ContactAdd(self):
        # 点击手动输入后进入添加成员列表
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        return ContactAdd