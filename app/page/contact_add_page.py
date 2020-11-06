from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.page.base_page import BasePage
from app.page.contact_menu_page import ContactMenu


class ContactAdd(BasePage):
    def add(self,name,gender,phone):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="必填"]').send_keys(name)
        # 此时需要设置显式等待以防弹窗未出现
        def mycondition(x):
            isExit = self.isElementExist(MobileBy.XPATH, '//*[@text="女"]')
            if isExit != True:
                self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()
                return False
            else:
                return True
        WebDriverWait(self.driver, 10).until(mycondition)
        self.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        return ContactMenu