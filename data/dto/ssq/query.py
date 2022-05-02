# 请求头
from datetime import datetime

from api.index import ApiPageDataRespBobdy
from api.page.index import PageInfo


# 查询请求体
class ApiQuerySsqReqBody(object):
    pageInfo: PageInfo = PageInfo()
    formParam = None


# 查询请求体
class ApiQuerySsqRespBody(ApiPageDataRespBobdy):
    pageInfo: PageInfo = PageInfo()
    data = []
