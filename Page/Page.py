from Page.add_user_page import Add_User_Page

class Page_Obj:
    def __init__(self,driver):
        self.driver = driver

    def address_add_user(self):
        # 通讯录添加用户
        return Add_User_Page(self.driver)