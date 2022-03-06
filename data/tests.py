import re

from django.test import TestCase

from common.common import _print
from data.SsqService import SsqService


class TestSsqService(TestCase):
    def test_strreplace(self):
        str = "1,091,513,907"
        print(str)
        print(re.sub(r'[^\d.]', '', str))


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


