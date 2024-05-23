from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import os
import sys

def get_data_file_path(filename):
    # 获取打包后的临时路径或开发环境的相对路径
    if hasattr(sys, '_MEIPASS'):
        # 运行时在打包后的临时目录
        base_path = sys._MEIPASS
    else:
        # 开发环境中的当前目录
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, filename)


def getGqq(url, cookies, custom_headers):
    # 初始化 Chrome WebDriver，并设置请求头
    options = Options()
    options.add_argument('--headless')  # 无界面模式
    for key, value in custom_headers.items():
        options.add_argument(f"--{key}={value}")
    service = Service("chromedriver.exe")  # 指定 Chrome WebDriver 路径
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # 添加 cookies
        driver.get(url)  # 先访问一次网站，确保会话建立
        parsed_url = urlparse(url)
        for name, value in cookies.items():
            driver.add_cookie({'name': name, 'value': value, 'domain': parsed_url.hostname})

        # 等待页面上的特定元素加载完成
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'script[src]')))

        # 执行 JavaScript 代码，获取动态变量
        dynamic_variable = driver.execute_script("return g_qq;")

        return dynamic_variable
    finally:
        # 关闭浏览器
        driver.quit()
