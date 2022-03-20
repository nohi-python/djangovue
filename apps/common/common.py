# -*- coding : utf-8 -*-
# coding: utf-8


# 打印公共方法
import re


def tostr(_str):
    _tmp = _str
    if type(_str) is tuple:
        _tmp = ''
        for i in range(len(_str)):
            _tmp = _tmp + ' ' + str(_str[i])
    return _tmp


# 打印
def _print(msg, *args):
    if args is None or len(args) == 0:
        # logging.debug(msg)
        print(tostr(msg))
    elif len(args) == 1:
        print(tostr(msg), args)
    else:
        # logging.debug('%s %s' % (msg, args))
        print('%s %s' % (tostr(msg), args))


# 删除非数字字符
def justDecimal(_str):
    if _str is None or len(_str) == 0:
        return 0
    else:
        return re.sub(r'[^\d.]', '', _str)


# 读取文件
def readfile(path, charSet='gbk'):
    _print("path:", path)
    # 模拟
    file_name = path
    content = ''
    try:
        with open(file_name, 'r', encoding=charSet) as f:
            content = content + f.read()
    finally:
        if f:
            f.close()
    _print("content:", content)
    return content
