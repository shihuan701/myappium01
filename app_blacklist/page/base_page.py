from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    black_lists = [(MobileBy.ID,'com.xueqiu.android:id/iv_close')]
    max_num = 3
    error_num = 0
    def __init__(self,driver:WebDriver=None):
            self.driver = driver

    def find(self,by,locate=None):
        try:
            if locate is None:
                ele = self.driver.find_element(*by)
            else:
                ele = self.driver.find_element(by,locate)
            self.error_num = 0
            return ele
        except Exception as e:
            if self.error_num > self.max_num:
                raise e
            self.error_num +=1
            for bl in self.black_lists:
                ele = self.driver.find_elements(*bl)

                if len(ele)>0:
                    ele[0].click()
                    return self.find(by,locate)
            raise e



    def wait_for_condition(self,timeout,mycondition):
        element:WebElement =WebDriverWait(self.driver,timeout).until(mycondition)
        return element

    def find_by_roll(self,text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                         .scrollable(true).instance(0))\
                                         .scrollIntoView(new UiSelector()\
                                         .text("{text}").instance(0));')

    def isElementExist(self,by,locate):
        flag = True
        try:
            self.find(by, locate)
            return flag
        except:
            flag = False
            return flag

    def get_toast(self):
        toast_txt = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return toast_txt







