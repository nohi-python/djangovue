from django.urls import path

from . import views

# 设置命名空间
app_name = 'data'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:qiCi>/', views.detail, name='detail'),
    path('<str:qiCi>/results', views.results, name='results'),

    # 获取JSON数据
    path('infoList', views.infoList, name='infoList'),
    path('json/respJson1', views.respJson1, name='respJson1'),
    path('json/respJson2', views.respJson2, name='respJson2'),
    path('json/respJson3', views.respJson3, name='respJson3'),
    path('json/respJson4', views.respJson4, name='respJson4'),
    # 数据更新
    path('dataRefresh', views.dataRefresh, name='dataRefresh'),
]