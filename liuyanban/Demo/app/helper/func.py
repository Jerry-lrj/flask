# 辅助函数

import re
import json

# 返回格式化输出
def ajaxReturn(info,data={}):
    info['data'] = data
    return json.dumps(info)

# 验证用户名的合法性
def check_username_legitimate(username):
    data = re.search(u'^[_a-zA-Z0-9\u4e00-\u9fa5]+$', username)
    if not data:
        return False
    return True

# 获取用户ip地址
def get_ip():
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    return ip