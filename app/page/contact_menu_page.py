from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage



class ContactMenu(BasePage):
    def goto_ContactAdd(self):
        # 点击手动输入后进入添加成员列表
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        from app.page.contact_add_page import ContactAdd
        return ContactAdd(self.driver)

    def get_toast(self):
        toast_txt = self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text
        return toast_txt