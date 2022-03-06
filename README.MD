.# README
> create by nohi 20220108

## 参考：
> https://wangxin1248.github.io/python/2019/08/django-vue.html

## 配置
* 数据库：
* eslint
    *  yarn add eslint eslint-config-airbnb eslint-plugin-import eslint-plugin-vue -D
    
### 模型
* python3 manage.py makemigrations 创建模型
* python3 manage.py makemigrations DjangoVue  # 让 Django 知道我们在我们的模型有一些变更

  ```
  python manage.py makemigrations polls（appname）
  ```
* python3 manage.py migrate polls （appname）  # 创建表结构
* 以上步骤都得执行 *



### 管理工具
* python3 manage.py createsuperuser 来创建超级用户

## 开发
* 前端：yarn dev
* 后端: python manage.py runserver

## 部署

## 版本
###