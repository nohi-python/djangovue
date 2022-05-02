import json
import re
from collections import namedtuple
from json import JSONEncoder

from django.test import TestCase

from api.index import ApiResponse, ClassEncoder
from api.page.index import PageInfo
from common.common import _print
from data.SsqService import SsqService
from dto.ssq.query import ApiQuerySsqRespBody
import json
from types import SimpleNamespace as Namespace

class TestSsqService(TestCase):
    def test_strreplace(self):
        _str = (1,2)
        print(_str)
        if type(_str) is tuple:
            print(len(_str))
            _tmp = ''
            for i in range(len(_str)) :
                print(i)
                _tmp = _tmp + ' ' + str(_str[i])
        print(_tmp)
        _str = "1,091,513,907"
        print(_str)
        print(re.sub(r'[^\d.]', '', _str))


    def test_getPage(self):
        print('======')
        _print('===start====')
        ssqService = SsqService()
        ssqService.get_page()
        _print('===over====')

    def test_save(self):
        print('======')
        _print('===start====')
        ssqService = SsqService()
        ssqService.dataRefresh('22001', '22002')
        _print('===over====')

    def custClassDecoder(item):
        return namedtuple('X', item.keys())(*item.values())

    def test_json(self):
        respInfo = ApiResponse()
        respBody = ApiQuerySsqRespBody()
        pageInfo = PageInfo()
        pageInfo.currentPage = 1
        pageInfo.pageSize = 10
        pageInfo.totalPage = 4


        print(pageInfo.__dict__)
        json_str = json.dumps(pageInfo.__dict__)
        print(json_str)
        print('=============================')
        respInfo.header.tranCode = '01'
        print(respInfo.header.tranCode)
        print(respInfo.__dict__)
        json_str = json.dumps(respInfo, indent=4, cls=ClassEncoder, ensure_ascii=False)
        print(json_str)

        respInfo = json.loads(json_str, object_hook=lambda d: Namespace(**d))
        print('after loads')
        print(respInfo.header.tranCode, respInfo.header.reqTime)
