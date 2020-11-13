from appium.webdriver.common.mobileby import MobileBy

from app_blacklist.page.base_page import BasePage


class MarketPage(BasePage):


    def goto_search_page(self):
        self.find(MobileBy.ID, 'com.xueqiu.android:id/action_search').click()
        from app_blacklist.page.search_page import Search
        return Search(self.driver)


