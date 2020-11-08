from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self,driver:WebDriver=None):
            self.driver = driver

    def find(self,by,locate):
        return self.driver.find_element(by,locate)


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







