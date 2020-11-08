from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BasePage():
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "True",
                "automationName":"uiautomator2"
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def stop(self):
        self.driver.quit()



