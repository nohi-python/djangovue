import json

import simplejson as simplejson
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import connection
# from django.db.models import Q
from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from api.index import ApiPageDataRespBobdy, ApiResponse, ClassEncoder
from api.page.index import PageInfo
from dto.ssq.query import ApiQuerySsqRespBody
from .DltService import DltService
from common.common import _print

# Create your views here.
from .models import SsqModel, DltModel
from .SsqService import SsqService
from types import SimpleNamespace as Namespace


def index(request):
    data_list = SsqModel.objects.order_by('-kaiJiangRiQi')[:5]
    output = ','.join([q.question_text for q in data_list])
    # 直接返回内容
    # return HttpResponse(output)

    template = loader.get_template('data/index.html')
    context = {
        'data_list': data_list,
    }

    # 快捷函数： render()
    return render(request, 'data/index.html', context)


# 期次详情
def detail(request, qiCi):
    # 尝试获取一个对象，如果不存在则返回 404
    # get_list_or_404()  get_object_or_404()
    print('qiCi: %s ' % (qiCi))
    dataItem = SsqModel.objects.filter(qiCi=qiCi).first()
    print('================ %s ' % (dataItem == None))

    if dataItem != None:
        print('%s, %s ' % (dataItem.id, dataItem.qiCi))
        dataItemJson = dataItem.__str__()
    return render(request, 'data/detail.html', {'dataItem': dataItem, 'dataItemJson': dataItemJson})


# 获取期次详情
def results(request, qiCi):
    response = "Your're looking at result of question %s"
    detaItem = get_object_or_404(SsqModel, qiCi=qiCi)
    print('detaItem is null ? : %s' % (detaItem == None))
    print("detaItem: %s" % detaItem)

    # 单个对象转json
    jsonData = model_to_dict(detaItem)
    return render(request, 'data/results.html', {'detaItem': detaItem, 'jsonData': jsonData})


def infoList(request):
    try:
        infoList = SsqModel.objects.all()
        print('infoList.length:%s' % (len(infoList)))
    except (KeyError, SsqModel.DoesNotExist):
        # Redisplay the question voting form.
        # return HttpResponseRedirect(reverse('data:results', args=('nonexxx',)))
        # return HttpResponse(choiceList)
        infoList = []
    # return HttpResponseRedirect(reverse('data:results', args=(choiceList,)))

    return HttpResponse(infoList)


# 返回JSON
# http://127.0.0.1:8000/data/json/respJson1
def respJson1(request):
    respInfo = {"code": "SUC", "msg": "这是中文1...", "infoList": [], "infoListStr": ""}
    return HttpResponse(json.dumps(respInfo), content_type='application/json')


# 返回JSON
def respJson2(request):
    respInfo = {"code": "SUC", "msg": "这是中文1respJson2...", "infoList": [], "infoListStr": ""}
    return JsonResponse(respInfo, safe=False, content_type='application/json')


# MODEL 返回JSON1
def respJson3(request):
    try:
        infoList = SsqModel.objects.all()
        print('infoList.length:%s' % (len(infoList)))
    except (KeyError, SsqModel.DoesNotExist):
        # Redisplay the question voting form.
        # return HttpResponseRedirect(reverse('data:results', args=('nonexxx',)))
        # return HttpResponse(choiceList)
        infoList = []
    # return HttpResponseRedirect(reverse('data:results', args=(choiceList,)))

    # 2. 将数据序列化成json格式   date类型的数据不能直接系列化 ensure_ascii=False 修改乱码的现象
    data = serializers.serialize('json', queryset=infoList)
    # 3. 返回
    return HttpResponse(data, content_type='application/json')


# MODEL 返回JSON1
def respJson4(request):
    respInfo = {"code": "SUC", "msg": "ok...", "infoList": []}
    try:
        infoList = SsqModel.objects.all()
        print('infoList.length:%s' % (len(infoList)))
    except (KeyError, SsqModel.DoesNotExist):
        infoList = []

    # 2. 将数据序列化成json格式   date类型的数据不能直接系列化 ensure_ascii=False 修改乱码的现象
    respInfo["infoList"] = json.loads(serializers.serialize('json', queryset=infoList))
    # 3. 返回
    return HttpResponse(json.dumps(respInfo), content_type='application/json')


# 数据初始化任务
def ssqDataRefreshJob(request):
    respInfo = {"code": "SUC", "msg": "ok...", "infoList": []}
    cursor = connection.cursor()
    cursor.execute("select max(qiCi) from data_ssqmodel")
    raw = cursor.fetchone()
    _print(raw)
    startQiCi = raw[0]
    endQiCi = '23001'
    print(startQiCi)
    _print('[%s-%s]' % (startQiCi, endQiCi))

    ssqService = SsqService()
    ssqService.dataRefresh(startQiCi, endQiCi)
    return HttpResponse(json.dumps(respInfo), content_type='application/json')


# 数据初始化
def ssqDataRefresh(request):
    respInfo = {"code": "SUC", "msg": "ok...", "infoList": []}
    # 获取数据
    _print("request.method:", request.method)
    for item in request.GET.keys():
        print("GET[%s][%s]" % (item.__str__(), request.GET.get(item)))

    if request.method == 'POST':
        req = simplejson.loads(request.body)
        print(req)
        for item in request.POST.keys():
            print("[%s][%s]" % (item.__str__(), request.GET.get(item)))

    startQiCi = request.GET.get("startQiCi")
    endQiCi = request.GET.get("endQiCi")

    ssqService = SsqService()
    ssqService.dataRefresh(startQiCi, endQiCi)

    # 返回JSON
    infoList = SsqModel.objects.all()
    # 2. 将数据序列化成json格式   date类型的数据不能直接系列化 ensure_ascii=False 修改乱码的现象
    respInfo["infoList"] = json.loads(serializers.serialize('json', queryset=infoList))
    # 3. 返回
    return HttpResponse(json.dumps(respInfo), content_type='application/json')


# 数据初始化任务
def dltDataRefreshJob(request):
    respInfo = {"code": "SUC", "msg": "ok...", "infoList": []}
    cursor = connection.cursor()
    cursor.execute("select max(qiCi) from data_dltmodel")
    raw = cursor.fetchone()
    _print(raw)
    startQiCi = raw[0]
    endQiCi = '23001'
    print(startQiCi)
    _print('[%s-%s]' % (startQiCi, endQiCi))

    service = DltService()
    service.dataRefresh(startQiCi, endQiCi)
    return HttpResponse(json.dumps(respInfo), content_type='application/json')


# 数据初始化
def dltDataRefresh(request):
    respInfo = {"code": "SUC", "msg": "ok...", "infoList": []}
    # 获取数据
    _print("request.method:", request.method)
    for item in request.GET.keys():
        print("GET[%s][%s]" % (item.__str__(), request.GET.get(item)))

    if request.method == 'POST':
        req = simplejson.loads(request.body)
        print(req)
        for item in request.POST.keys():
            print("[%s][%s]" % (item.__str__(), request.GET.get(item)))

    startQiCi = request.GET.get("startQiCi")
    endQiCi = request.GET.get("endQiCi")

    service = DltService()
    service.dataRefresh(startQiCi, endQiCi)

    # 返回JSON
    infoList = DltModel.objects.all()
    # 2. 将数据序列化成json格式   date类型的数据不能直接系列化 ensure_ascii=False 修改乱码的现象
    respInfo["infoList"] = json.loads(serializers.serialize('json', queryset=infoList))
    # 3. 返回
    return HttpResponse(json.dumps(respInfo), content_type='application/json')


# 双色球列表
def ssqList(request):
    respInfo = ApiResponse()
    respBody = ApiQuerySsqRespBody()
    respInfo.body = respBody

    # 获取数据
    _print("request.method:", request.method)
    for item in request.GET.keys():
        print("GET[%s][%s]" % (item.__str__(), request.GET.get(item)))
    reqInfo = {}
    if request.method == 'POST':
        req = simplejson.loads(request.body)
        _print('reqbody:%s' % req)
        _print('typeof:%s', type(req))
        reqInfo = req
    _print('reqInfo:', json.dumps(reqInfo, cls=ClassEncoder))

    formParm = reqInfo['body']['formParm']

    where = Q()
    if formParm['lastQiCi'] is None or formParm['lastQiCi'] == '':
        if formParm['qiCiStart'] is not None and formParm['qiCiStart'] != '':
            q = Q(qiCi__gte=formParm['qiCiStart'])
            where.add(q, Q.AND)
        if formParm['qiCiEnd'] is not None and formParm['qiCiEnd'] != '':
            q = Q(qiCi__lte=formParm['qiCiEnd'])
            where.add(q, Q.AND)
        if formParm['dataStart'] is not None and formParm['dataStart'] != '':
            q = Q(kaiJiangRiQi__gte=formParm['dataStart'])
            where.add(q, Q.AND)
        if formParm['dataEnd'] is not None and formParm['dataEnd'] != '':
            q = Q(kaiJiangRiQi__lte=formParm['dataEnd'])
            where.add(q, Q.AND)
        # 返回JSON
        infoList = SsqModel.objects.all().order_by('-kaiJiangRiQi').filter(where)
        _print('数据记录数', len(infoList))

    # 分页数据
    pageInfo = reqInfo['body']['pageInfo']
    if pageInfo is None:
        pageInfo = PageInfo()
    else:
        pageInfo = json.loads(json.dumps(pageInfo), object_hook=lambda d: Namespace(**d))
    _print('pageInfo', json.dumps(pageInfo, indent=4, cls=ClassEncoder, ensure_ascii=False))

    lastNum = 0
    if formParm['lastQiCi'] == 'ten':
        lastNum = 10
    elif formParm['lastQiCi'] == 'twenty':
        lastNum = 20
        pageInfo.pageSize = 20
    elif formParm['lastQiCi'] == 'hundred':
        lastNum = 100
        pageInfo.pageSize = 100

    _print('lastNum:', lastNum)
    if lastNum > 0:
        lastNum = lastNum
        # 返回JSON
        infoList = SsqModel.objects.all().order_by('-kaiJiangRiQi')
        _print('数据记录数1:', len(infoList))
        infoList = infoList[:lastNum]
        _print('数据记录数2:', len(infoList))

    print('where===')
    print(where)

    paginator = Paginator(infoList, pageInfo.pageSize)  # 每页显示10条
    pageInfo.totalRow = paginator.count
    try:
        infoList = paginator.page(pageInfo.currentPage)  # paginator.page(page)获取第page页
    except PageNotAnInteger:
        infoList = paginator.page(1)  # 如果请求页数不是整数，返回第一页
    except EmptyPage:
        infoList = paginator.page(paginator.num_pages)  # 如果请求的页数不在范围内则返回最后一页
    # 2. 将数据序列化成json格式   date类型的数据不能直接系列化 ensure_ascii=False 修改乱码的现象
    respBody.data = json.loads(serializers.serialize('json', queryset=infoList))
    respBody.pageInfo = pageInfo
    # 3. 返回
    return HttpResponse(json.dumps(respInfo, indent=4, cls=ClassEncoder, ensure_ascii=False),
                        content_type='application/json')
