import os

from selenium import webdriver

from requests_html import HTML

# 浏览器选项
options = webdriver.ChromeOptions()

# 设置为 headless 模式（不显示界面）
# options.add_argument("--headless")

# 忽略SSL证书错误
options.add_argument('--ignore-certificate-errors')

# 隐藏提示信息栏
options.add_argument('disable-infobars')
'''
# 禁止加载图片
prefs = {
    "profile.managed_default_content_settings.images": 2
}
# 禁用密码保存提示
prefs['credentials_enable_service'] = False
prefs['profile'] = {
    'password_manager_enabled': False
}

options.add_experimental_option("prefs", prefs)
'''
# 驱动路径
driver_path = os.path.join(os.getcwd(), r'chromedriver.exe')

# 实例化浏览器
browser = webdriver.Chrome(
    executable_path=driver_path,
    chrome_options=options
)

# ###############################################################
# 打开登录页
browser.get('http://learning.cqzuxia.com/home/login')

# 获取属性
# get_attribute()

# 获取用户名输入框
e_username = browser.find_element_by_css_selector('#username')
# 清空现有用户名
e_username.clear()
# 输入用户名
e_username.send_keys("22506")

# 获取密码输入框
e_password = browser.find_element_by_css_selector('#password')
# 清空现有密码
e_password.clear()
# 输入密码
e_password.send_keys('283111')

# 触发登录按钮点击
browser.find_element_by_css_selector('.btn-login').click()

# 获取用户姓名
student_name = browser.find_element_by_css_selector('.student-name').text.strip()

''''
# 获取当前页面URL和页面源码（经过渲染之后的），传递给Requests-HTML
html = HTML(url=browser.current_url, html=browser.page_source)
# 查找元素
'''
# 点击"评估系统"
browser.find_element_by_css_selector('.kp a').click()

# 获取课程列表
e_kecheng_list = browser.find_elements_by_css_selector('[data-bind="foreach: courseList"] > div')
# 要查找的课程名
filter_name = 'Web前端框架开发技术'
def filter_kecheng(kecheng_item):
    '''筛选指定的课程'''
    global filter_name
    # 获取课程名
    kecheng_name = kecheng_item.find_element_by_css_selector('.book-title').text.strip()
    return filter_name in kecheng_name
# 筛选
e_web_kecheng = list(filter(filter_kecheng, e_kecheng_list))[0]
# 跳转到课程详情
e_web_kecheng.find_element_by_css_selector('.book-item').click()