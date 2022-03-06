# -*- coding : utf-8 -*-
# coding: utf-8
import logging
import random
import traceback

import requests
from bs4 import BeautifulSoup
from django.core import serializers
from django.shortcuts import get_object_or_404

from common.common import _print, justDecimal
from common.config.config import configs
from common.exception.exception import ServiceException
from common.ippool.proxypool import IPProxyPool
from data.models import SsqModel


class SsqService():
    def __init__(self):  # 类的初始化操作
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.USER_AGENTS = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
        ]
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
            ssqItme = SsqModel()
            ssqItme.qiCi = tds[0].text
            ssqItme.hongYi = tds[1].text
            ssqItme.hongEr = tds[2].text
            ssqItme.hongSan = tds[3].text
            ssqItme.hongSi = tds[4].text
            ssqItme.hongWu = tds[5].text
            ssqItme.hongLiu = tds[6].text
            ssqItme.langQiu = tds[7].text
            ssqItme.jiangChiJinEr = justDecimal(tds[9].text)
            ssqItme.yiDengJiangZhuShu = tds[10].text
            ssqItme.yiDengJiangJiangJin = justDecimal(tds[11].text)
            ssqItme.erDengJiangZhuShu = tds[12].text
            ssqItme.erDengJiangJiangJin = justDecimal(tds[13].text)
            ssqItme.kaiJiangRiQi = tds[15].text
            ssqList.append(ssqItme)

        _print('数据:', serializers.serialize('json', ssqList))
        # _print('数据:', json.dumps(ssqList))
        return ssqList

    # 保存数据
    def saveSsqModel(self, ssqItme : SsqModel):
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