from django.urls import path

from . import views

# 设置命名空间
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail1'),

    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),

    # 获取JSON数据
    path('questionJsonOne', views.questionJsonOne, name='questionJsonOne'),
    path('questionJsonTwo', views.questionJsonTwo, name='questionJsonTwo'),
    path('questionList', views.questionList, name='questionList'),
]