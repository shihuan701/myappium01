from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage



class PreContactEdit(BasePage):
    def goto_ContactEdit(self,name):

        '''
        # 1.滚动查找目标行
          2.点击编辑按钮
        :return:
        '''
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));')
        print(f'//*[@text="{name}"]/../../../../android.widget.RelativeLayout')
        self.driver.find_element(MobileBy.XPATH,f'//*[@text="{name}"]/../../../../android.widget.RelativeLayout').click()
        from app.page.contact_edit_page import ContactEdit
        return ContactEdit(self.driver)

    def checkuser(self,name):
        flag = True
        try:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));')
            return flag
        except:
            flag = False
            return flag

