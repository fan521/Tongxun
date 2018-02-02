import sys,os
sys.path.append(os.getcwd())

from  Base.InitDriver import init_driver
from Page.Page import Page_Obj
import pytest

from Base.Read_Data import ret_yaml_data

def yaml_data():
    data_list = []
    data = ret_yaml_data("address_data.yml").get("Address_Data:")
    for i in data.keys():
        data_list.append((i, data.get(i).get("test_name"),data.get(i).get("test_phone"),data.get(i).get("expect_data")))
    return data_list

class Test_Add_User:
    def setup_class(self):
        self.driver = init_driver()
        self.add_user_obj = Page_Obj(self.driver).address_add_user()

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture()
    def add_user_btn(self):
    #     点击添加用户按钮
        self.add_user_obj.click_add()

    # @pytest.fixture(scope="class")
    # def save_local_btn(self):
    #     # 点击本地保存
    #     self.add_user_obj.click_save_local()

    @pytest.mark.usefixtures("add_user_btn")
    # @pytest.mark.usefixtures("add_user_btn", "save_local_btn")
    @pytest.mark.parametrize("test_num,test_name,test_phone,expect_data",yaml_data())
    def test_input_user_info(self,test_num,test_name,test_phone,expect_data):
        self.add_user_obj.input_user_info(test_name,test_phone)
        print("test_001", test_num)
        if test_num == "test_001":
            assert expect_data not in  self.add_user_obj.get_user_list()
        else:
            assert expect_data in self.add_user_obj.get_user_list()
        # self.driver.get_screenshot_as_file("./screen/%s.png" % test_num)
