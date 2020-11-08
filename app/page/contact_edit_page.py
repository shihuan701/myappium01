from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage



class ContactEdit(BasePage):
    def delete(self):
        self.find(MobileBy.XPATH,'//*[@text="删除成员"]').click()
        self.find(MobileBy.XPATH, '//*[@text="确定"]').click()
        from app.page.contact_preedit_page import PreContactEdit
        return PreContactEdit(self.driver)

