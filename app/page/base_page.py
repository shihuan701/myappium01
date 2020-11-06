from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BasePage():
    def __init__(self,driver:WebDriver=None):
        caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "True"
        }
        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hud',caps)
        self.driver.implicitly_wait(5)



