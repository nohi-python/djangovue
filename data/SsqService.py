# -*- coding : utf-8 -*-
# coding: utf-8
import logging
import random
import traceback

import requests
from bs4 import BeautifulSoup
from django.core import serializers

from common.common import _print, justDecimal, readfile
from common.config.config import configs
from common.exception.exception import ServiceException
from common.ippool.proxypool import IPProxyPool
from .models import SsqModel


class SsqService():
    def __init__(self):  # 类的初始化操作
        self.headers = configs.headers
        self.USER_AGENTS = configs.USER_AGENTS
        self.web_url = 'https://www.dy2018.com'  # 地址网站
        # self.web_url_first = 'http://datachart.500.com/ssq/history/newinc/history.php?start=03001&end=22023'  # 要访问的网页地址
        self.web_url_first = 'http://datachart.500.com/ssq/history/newinc/history.php?start=22001&end=22023'  # 要访问的网页地址
        self.web_url_pattern = 'http://datachart.500.com/ssq/history/newinc/history.php?start=%s&end=%s'  # 要访问的网页地址
        self.folder_path = configs.folder_path  # 设置图片要存放的文件目录
        self.ippool = IPProxyPool()
        # self.ippool = IPProxyPool_XXY()

    def request(self, url):  # 返回网页的response
        headers = {
            'User-Agent': random.choice(self.USER_AGENTS),
            # ':authority': 'www.dy2018.com',
            # ':method': 'GET',
            # ':path': '/html/gndy/dyzz/index.html',
            # ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://www.dy2018.com/html/gndy/dyzz/index.html',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        print(headers)
        # proxies = self.ippool.get_proxies()
        # r = requests.get(url, proxies=proxies, headers=headers, verify=False)  # 像目标url地址发送get请求，返回一个response对象
        r = requests.get(url, headers=headers, verify=False, timeout=(10, 30))  # 像目标url地址发送get请求，返回一个response对象
        return r

    # 获取页面
    def get_page(self, startQiCi, endQiCi):
        _print('获取页面,期次[%s]-[%s]' % (startQiCi, endQiCi))
        # url = self.web_url_first
        if startQiCi > endQiCi:
            url = self.web_url_pattern % (endQiCi, startQiCi)
        else:
            url = self.web_url_pattern % (startQiCi, endQiCi)
        _print('获取页面URL[%s]' % url)
        try:
            r = self.request(url)
        except Exception as r:
            traceback.print_exc()
            _print('未知错误 %s', r)
            raise ServiceException("ServiceException", "获取页面异常")

        content = r.content.decode('utf-8')
        if r.encoding == 'utf-8':
            content = r.content.decode('utf-8')
        else:
            content = r.content.decode('utf-8')

        # 模拟
        # file_name = '/Users/nohi/work/workspaces-seed/billions/datafile/ssq.html'
        # content = readfile(file_name, 'utf-8')

        logging.debug("解析文件内容 start")
        # 安装 lxml: pip install -i https://pypi.douban.com/simple lxml
        all_tr = BeautifulSoup(content, 'lxml').select('#tdata tr')  # 获取网页中的class为cV68d的所有a标签
        if not all_tr or len(all_tr) == 0:
            _print('结果为空')
            return
        else:
            _print('all_a', len(all_tr))

        # p1 = re.compile(r'[《](.*?)[》]', re.S)  # 最小匹配
        ssqList = []
        for tr in all_tr:
            tds = tr.select('td')
            ssqItem = SsqModel()
            ssqItem.qiCi = tds[0].text
            ssqItem.hongYi = tds[1].text
            ssqItem.hongEr = tds[2].text
            ssqItem.hongSan = tds[3].text
            ssqItem.hongSi = tds[4].text
            ssqItem.hongWu = tds[5].text
            ssqItem.hongLiu = tds[6].text
            ssqItem.langQiu = tds[7].text
            ssqItem.jiangChiJinEr = justDecimal(tds[9].text)
            ssqItem.yiDengJiangZhuShu = tds[10].text
            ssqItem.yiDengJiangJiangJin = justDecimal(tds[11].text)
            ssqItem.erDengJiangZhuShu = tds[12].text
            ssqItem.erDengJiangJiangJin = justDecimal(tds[13].text)
            ssqItem.zongTouZhuEr = justDecimal(tds[14].text)
            ssqItem.kaiJiangRiQi = tds[15].text
            ssqList.append(ssqItem)

        _print('数据:', serializers.serialize('json', ssqList))
        # _print('数据:', json.dumps(ssqList))
        return ssqList

    # 保存数据
    def saveSsqModel(self, ssqItme: SsqModel):
        _print('保存数据开始:', ssqItme.qiCi)
        dataItem = SsqModel.objects.filter(qiCi=ssqItme.qiCi).first()
        if dataItem is None:
            ssqItme.save()
        else:
            _print('保存数据,其次数据存在，其次::', ssqItme.qiCi)

    # 保存数据
    def saveSsqList(self, ssqList):
        _print('保存数据列表开始:', len(ssqList))
        i = 0
        for item in ssqList:
            i = i + 1
            if i % 10 == 0:
                _print('保存[%s]:' % i)
            try:
                self.saveSsqModel(item)
            except Exception as e:
                logging.exception(e)
                continue

    # 数据初始化
    def dataRefresh(self, startQiCi, endQiCi):
        _print('数据初始化,期次[%s]-[%s]' % (startQiCi, endQiCi))

        # 获取数据
        ssqList = self.get_page(startQiCi, endQiCi)
        _print('数据列表大小:', len(ssqList))

        # 保存数据
        self.saveSsqList(ssqList)
