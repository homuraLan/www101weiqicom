
from requests.structures import CaseInsensitiveDict
from itertools import islice

def headers_str_to_dict():
    try:
        request_headers = {}
        with open('headers.txt',encoding='utf-8',mode='r') as file:
        #with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                # 使用 islice 读取两行
                lines = list(islice(file, 2))
                if not lines:
                    break
                # 处理两行
                if len(lines) == 2:
                    line1, line2 = lines
                    request_headers[line1.strip().replace(':','')]=line2.strip()
                else:
                    line1 = lines[0]
                    print(f"Processing single line: {line1.strip()}")
        return request_headers
    except Exception as e:
        print(f"An error occurred: {e}")


# 解析Cookie为字典
def parse_cookie(cookie_str):
    # 初始化空字典
    cookies_dict = {}

    # 拆分每个键值对并添加到字典中
    for cookie in cookie_str.split('; '):
        if '=' in cookie:
            key, value = cookie.split('=', 1)
            cookies_dict[key] = value

    return cookies_dict

