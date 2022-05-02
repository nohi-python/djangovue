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

* ModuleNotFoundError: No module named 'common'
  * settings.py 增加： sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))   common在上层目录


### 管理工具
* python3 manage.py createsuperuser 来创建超级用户

## 开发
* 前端：yarn dev
* 后端: python manage.py runserver

### api
* json
  - http://127.0.0.1:8000/data/json/respJson1
  - http://127.0.0.1:8000/data/json/respJson2
  - http://127.0.0.1:8000/data/json/respJson3
  - http://127.0.0.1:8000/data/json/respJson4
* ssq
  * 期次详情：
      http://127.0.0.1:8000/data/22001/
      http://127.0.0.1:8000/data/22001/results
  * 列表数据：
      http://127.0.0.1:8000/data/json/respJson3
      http://127.0.0.1:8000/data/json/respJson4
  * 数据刷新
    * 双色球 数据刷新 startQiCi 开始期次   endQiCi结束期次
      * POST http://{{server}}/data/ssqDataRefresh?startQiCi=03001&endQiCi=22001
    * 双色球 数据刷新 定时任务
      * GET http://{{server}}/data/ssqDataRefreshJob
      
## 部署

## 版本
###