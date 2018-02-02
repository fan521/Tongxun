from selenium.webdriver.common.by import By
"""
    添加通讯录
"""
# 添加用户按钮
add_user = (By.ID, "com.android.contacts:id/floating_action_button")
# 点击本地保存
save_local = (By.XPATH, "//*[contains(@text,'本地')]")
# 用户text
user_text = (By.ID, "com.android.contacts:id/cliv_name_textview")
# 定位姓名
send_name = (By.XPATH, "//*[contains(@text,'姓名')]")
# 定位手机号
send_phone = (By.XPATH, "//*[contains(@text,'电话')]")
# 点击返回保存按钮
click_save_back = (By.XPATH, "//*[contains(@content-desc,'向上导航')]")
# 定位用户详情页编辑按钮
edit_text = (By.ID, "com.android.contacts:id/menu_edit")