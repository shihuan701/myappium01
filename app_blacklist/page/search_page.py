from appium.webdriver.common.mobileby import MobileBy

from app_blacklist.page.base_page import BasePage


class Search(BasePage):


    def search(self):
        # self.find(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/search_input_text"]')
        self.parse_yaml(path='../steps/search_page.yml',name='search')



