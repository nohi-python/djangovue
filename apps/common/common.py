# -*- coding : utf-8 -*-
# coding: utf-8
import json
import logging


# 打印公共方法
import re


def _print(msg, *args):
    if args is None or len(args) == 0:
        # logging.debug(msg)
        print(msg)
    else:
        # logging.debug('%s %s' % (msg, args))
        print('%s %s' % (msg, args))


def justDecimal(str):
    if str is None or len(str) == 0:
        return 0
    else:
        return re.sub(r'[^\d.]', '', str)

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
    _print("content", content)
    return content