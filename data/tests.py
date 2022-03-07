import re

from django.test import TestCase

from common.common import _print
from data.SsqService import SsqService


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


