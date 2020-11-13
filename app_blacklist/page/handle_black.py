


def handle_black(func):
    def wrapper(*args,**kwargs):
        # args[0],表示函数的第1位参数，一般是self
        from app_blacklist.page.base_page import BasePage
        instance:BasePage = args[0]
        try:
            ele = func(*args,**kwargs)
            instance.error_num = 0
            return ele
        # 捕获黑名单中的元素
        except Exception as e:
            if instance.error_num > instance.max_num:
                raise e
            instance.error_num +=1
            # 依次遍历黑名单列表
            for bl in instance.black_lists:
                ele = instance.driver.find_elements(*bl)
                if len(ele)>0:
                    ele[0].click()
                    return wrapper(*args,**kwargs)
            raise e

    return wrapper