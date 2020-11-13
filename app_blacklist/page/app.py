import yaml
from appium import webdriver

from app_blacklist.page.base_page import BasePage
from app_blacklist.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            self.driver = webdriver.Remote(f'http://{ip}:{port}/wd/hub', caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)

with open('../datas/appconf.yml') as f:
    appconfig = yaml.safe_load(f)
    caps = appconfig['caps']
    ip = appconfig['server']['ip']
    port = appconfig['server']['port']