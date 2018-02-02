from appium import webdriver

def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.120.101:5555'
    desired_caps['deviceName'] = 'true'#不是初始化状态才能有效
    # app的信息
    desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    # 中文输入允许
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明我们的driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver