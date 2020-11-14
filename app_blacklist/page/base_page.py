import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from app_blacklist.page.handle_black import handle_black


class BasePage():
    black_lists = [(MobileBy.ID,'com.xueqiu.android:id/iv_close')]
    max_num = 3
    error_num = 0
    def __init__(self,driver:WebDriver=None):
            self.driver = driver

    @handle_black
    def find(self,by,locate=None):

        if locate is None:
            ele = self.driver.find_element(*by)
        else:
            ele = self.driver.find_element(by,locate)
        return ele




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

    def parse_yaml(self,path,name):
        with open(path,encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        steps = datas[name]
        self.parese(steps)

    '''
    此方法用于解析步骤
    '''
    def parese(self,steps):
        for step in steps:
            if step['action'] == 'click':
                self.find(step['by'], step['locate']).click()






