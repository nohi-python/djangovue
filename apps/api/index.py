import string
from datetime import datetime
from json import JSONEncoder

from django.utils import timezone
from api.page.index import PageInfo


# 请求头
class ApiHeader(object):
    # 交易码
    tranCode = '01'
    # 交易流水号
    reqFlow = ''
    # 请求时间
    reqTime = timezone.now
    # 响应时间
    respTime = timezone.now
    # 响应码
    respCode = 'SUC'
    # 响应信息
    respMsg = ''

    def __init__(self, tranCode='TC', reqFlow='', reqTime=None, respTime=None, respCode='SUC', respMsg = '') -> None:
        super().__init__()
        print('ApiHeader.init')
        self.tranCode = tranCode
        self.reqFlow = reqFlow
        self.reqTime = reqTime
        self.respTime = respTime
        self.respCode = respCode
        self.respMsg = respMsg


# 响应体
class ApiResponseBody(object):
    data = None

    def __init__(self, data=None) -> None:
        super().__init__()
        print('ApiResponseBody.data')
        self.data = data


# 响应体-分页数据
class ApiPageDataRespBobdy(ApiResponseBody):
    # 分页信息
    pageInfo = None

    def __init__(self, code='SUC', msg='', data=None, pageInfo: PageInfo = None) -> None:
        super().__init__()
        print('ApiPageDataRespBobdy.init')
        self.msg = msg
        if pageInfo is None:
            pageInfo = PageInfo()
        self.pageInfo = pageInfo


# ================== 公用请求响应定义  ==========================#
# 请求
class ApiRequest(object):
    header: ApiHeader = ApiHeader()
    body: object = None


# 响应
class ApiResponse(object):
    str_v1 = '1111'
    str_v2 = 2222
    header: ApiHeader = ApiHeader()
    body: ApiResponseBody = ApiResponseBody()

    def __init__(self, str_v1: string = '1', str_v2: string = '2', header: ApiHeader = ApiHeader(),
                 body: ApiResponseBody = ApiResponseBody()):
        self.str_v1 = str_v1
        self.str_v2 = str_v2
        self.header = header
        self.body = body


#
class ClassEncoder(JSONEncoder):
    def default(self, o): return o.__dict__
