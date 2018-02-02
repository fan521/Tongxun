from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element_I(self,loc, timeout=10, poll=0.5):

        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_element(*loc))

    def find_elements_I(self,loc, timeout=10, poll=0.5):

        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_elements(*loc))

    def if_disp(self):
    #     判断元素是否存在
        try:
            self.find_element_I(loc)
            return  True
        except Exception as e:
            return  False


    def click_element(self, loc):
        # 点击函数
        self.find_element_I(loc).click()

    def input_text(self, loc, text):
        ele = self.find_element_I(loc)
        ele.clear()
        ele.send_keys(text)