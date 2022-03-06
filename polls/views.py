import json

from django.core import serializers
from django.template import loader

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Question, Choice


# Create your views here.

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in lastest_question_list])
    # 直接返回内容
    # return HttpResponse(output)

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': lastest_question_list,
    }
    # 返回渲染对象
    # return HttpResponse(template.render(context, request))

    # 快捷函数： render()
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'data/detail.html', {'question': question})

    # 尝试获取一个对象，如果不存在则返回 404
    # get_list_or_404()  get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "Your're looking at result of question %s"
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def questionJsonOne(request):
    try:
        choiceList = [
            {'id': 'id_1', 'name': '张三', 'age': 18, 'addr': '中国南京1'},
            {'id': 'id_2', 'name': '李四', 'age': 28, 'addr': '中国南京2'},
            {'id': 'id_3', 'name': '王五', 'age': 38, 'addr': '中国南京3'},
            {'id': 'id_4', 'name': '赵六', 'age': 48, 'addr': '中国南京4'},
        ]
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        # return HttpResponseRedirect(reverse('data:results', args=('nonexxx',)))
        # return HttpResponse(choiceList)
        choiceList = []
    # return HttpResponseRedirect(reverse('data:results', args=(choiceList,)))

    return HttpResponse(json.dumps(choiceList))


def questionJsonTwo(request):
    try:
        choiceList = [
            {'id': 'id_1', 'name': '张三', 'age': 18, 'addr': '中国南京1'},
            {'id': 'id_2', 'name': '李四', 'age': 28, 'addr': '中国南京2'},
            {'id': 'id_3', 'name': '王五', 'age': 38, 'addr': '中国南京3'},
            {'id': 'id_4', 'name': '赵六', 'age': 48, 'addr': '中国南京4'},
        ]
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        # return HttpResponseRedirect(reverse('data:results', args=('nonexxx',)))
        # return HttpResponse(choiceList)
        choiceList = []
    # return HttpResponseRedirect(reverse('data:results', args=(choiceList,)))
    return JsonResponse(list(choiceList), safe=False)


def questionList(request):
    try:
        choiceList = Question.objects.order_by('-pub_date')[:5]
        print(choiceList)
        output = ','.join([q.question_text for q in choiceList])
        print(output)
        # 直接返回内容
        # return HttpResponse(output)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        # return HttpResponseRedirect(reverse('data:results', args=('nonexxx',)))
        # return HttpResponse(choiceList)
        choiceList = []
    # return HttpResponseRedirect(reverse('data:results', args=(choiceList,)))
    return HttpResponse(serializers.serialize('json', queryset=choiceList))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
