from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage



class PreContactEdit(BasePage):
    def goto_ContactEdit(self,name):

        '''
        # 1.滚动查找目标行
          2.点击编辑按钮
        :return:
        '''
        self.find_by_roll(text=name)
        self.find(MobileBy.XPATH,f'//*[@text="{name}"]/../../../../android.widget.RelativeLayout').click()
        from app.page.contact_edit_page import ContactEdit
        return ContactEdit(self.driver)

    def checkuser(self,name):
        flag = True
        try:
            self.find_by_roll(text=name)
            return flag
        except:
            flag = False
            return flag

