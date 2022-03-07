import json

import simplejson as simplejson
from django.core import serializers
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from SsqService import SsqService
from common.common import _print
from .models import SsqModel


# Create your views here.

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


def detail(request, qiCi):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'data/detail.html', {'question': question})

    # 尝试获取一个对象，如果不存在则返回 404
    # get_list_or_404()  get_object_or_404()
    print('qiCi: %s ' % ( qiCi ))
    dataItem = SsqModel.objects.filter(qiCi=qiCi).first()
    print('================ %s ' % (dataItem == None))

    if dataItem != None:
      print('%s, %s ' % (dataItem.id, dataItem.qiCi))
      dataItemJson = dataItem.__str__()
    return render(request, 'data/detail.html', {'dataItem': dataItem, 'dataItemJson': dataItemJson})


def results(request, qiCi):
    response = "Your're looking at result of question %s"
    dataitem = get_object_or_404(SsqModel, qiCi=qiCi)
    return render(request, 'data/results.html', {'dataItem': dataitem})


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
def dataRefreshJob(request):
    respInfo = {"code": "SUC", "msg": "ok...", "infoList": []}
    cursor = connection.cursor()
    cursor.execute("select max(qiCi) from data_ssqmodel")
    raw = cursor.fetchone()
    _print(raw)
    startQiCi = raw
    endQiCi = '23001'
    _print('[%s-%s]' % (startQiCi, endQiCi))

    ssqService = SsqService()
    # ssqService.dataRefresh(startQiCi, endQiCi)
    return HttpResponse(json.dumps(respInfo), content_type='application/json')


# 数据初始化
def dataRefresh(request):
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