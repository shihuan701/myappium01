import yaml
from appium.webdriver.common.mobileby import MobileBy

from app_blacklist.page.base_page import BasePage


class MainPage(BasePage):

    def goto_market_page(self):

        # 首页，点击下方行情按钮进如行情界面
        # 模拟一个弹窗
        '''
        self.find(MobileBy.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/post_status']").click()
        self.find(MobileBy.XPATH, "//*[@resource-id = 'android:id/tabs']//*[@text = '行情']").click()
        :return:
        '''
        # with open('../steps/main_page.yml',encoding='utf-8') as f:
        #     datas = yaml.safe_load(f)
        # steps = datas['goto_market_page']
        # for step in steps:
        #     if step['action'] == 'click':
        #         self.find(step['by'], step['locate']).click()
        self.parse_yaml(path='../steps/main_page.yml',name='goto_market_page')
        from app_blacklist.page.market_page import MarketPage
        return MarketPage(self.driver)