from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
import logging

class TestWework():
  logging.basicConfig(level=logging.INFO)
  def setup(self):
    logging.info('start -----------------------')
    capas = {
      "platformName": "Android",
      "deviceName": "46b86315",
      "appPackage": "com.tencent.wework",
      "appActivity": ".launch.LaunchSplashActivity",
      "noReset": "True"
    }
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capas)
    self.driver.implicitly_wait(5)

  def teardown(self):
    # self.driver.quit()
    pass

  def testdemo(self):
    self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
    self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,\
                             'new UiScrollable(new UiSelector().scrollable(true).instance(0))'\
                             '.scrollIntoView(new UiSelector()'\
                             '.text("打卡").instance(0));').click()
    self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
    self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
    WebDriverWait(self.driver,10).until(lambda d : '外出打卡成功' in self.driver.page_source)






