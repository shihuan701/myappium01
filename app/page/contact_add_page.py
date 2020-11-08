from appium.webdriver.common.mobileby import MobileBy


from app.page.base_page import BasePage



class ContactAdd(BasePage):


    def add(self,name,gender,phone):
        self.find(MobileBy.XPATH,'//*[@text="必填"]').send_keys(name)
        # 此时需要设置显式等待以防弹窗未出现
        def mycondition(x):
            isExit = self.isElementExist(MobileBy.XPATH, '//*[@text="女"]')
            if isExit != True:
                self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()
                return False
            else:
                return True
        self.wait_for_condition(timeout=10,mycondition=mycondition)
        self.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        self.find(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phone)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from app.page.contact_menu_page import ContactMenu
        return ContactMenu(self.driver)


