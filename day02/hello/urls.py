from django.urls import path, re_path
from hello import views
from hello import views1   # 导入views1，因为useradd子目录，处理其请求的为views1.py

app_name = 'hello'
urlpatterns = [
    # 普通URL参数
    # path('', views.index, name='index'),

# 简易的用户管理系统
    # (添加用户) 用户访问http://127.0.0.1:8001/hello/useradd/ , views1中得useradd函数处理请求
    path('useradd/', views1.useradd, name="useradd"),
    # （用户列表）用户访问http://127.0.0.1:8001/hello/userlist/,views1中的userlist函数处理请求
        # name="userlist",定义一个命名空间为userlist
    path('userlist/', views1.userlist, name="userlist"),
    # (用户更新) 用户访问http://127.0.0.1:8001/hello/modify/用户id/,views1中的modify函数处理请求
        # name="modify"，定义一个命名空间为modiy,供前端模板调用
            # 前端模板调用范例(APP名称+命名空间):<a href="{% url 'hello:modify' user.id %}">更新</a>
                # 这样调用方式好处就是灵活,后端的path路径可以随便变动,只要命名空间名称不变就好
                    #   'modify1111/(?P<pk>[0-9]+)?/', views1.modify, name="modify"
    re_path('modify/(?P<pk>[0-9]+)?/', views1.modify, name="modify"),
    # (用户删除) 用户访问http://127.0.0.1:8001/hello/modify/用户id/,views1中的modify函数处理请求
    re_path('userdel/(?P<pk>[0-9]+)?/', views1.userdel, name="userdel")
]



    # 位置匹配
    # re_path('([0-9]{4})/([0-9]{2})/', views.index, name='index')

    #关键字匹配(/2019/06/)
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index'),
