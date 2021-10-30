# 入口配置
import os

web_url = "http://101.251.192.227:5001/"  # 网站地址
username_text = 'test'
password_text = 'acctrue1'

current_path = os.path.abspath(os.path.dirname(__file__))
print(str(current_path).strip('config'))
screenshots_folder = os.path.join(str(current_path).strip('\\config') + "o\\photo\\")
print(screenshots_folder)
