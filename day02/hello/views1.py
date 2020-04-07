from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, QueryDict
from hello.models import User       # 导入module,模型即数据库表
import traceback                    # traceback模块被用来跟踪异常返回信息

# 处理urls.py中定义用户添加功能的函数
def useradd(request):
    """
        添加用户：（用户添加分为get请求和post请求）
         request获取表单提交的数据有多种方式：
        1、request.POST.get --> 适用于获取单个变量进行处理的场景
        2、request.POST.dict() --> 适用于将表单所有数据整体处理的场景
        3、From(request.POST) --> 适用于表单类验证的场景（生产中最常用）
    """
    msg = {}          # 自定义用户页面返回信息（成功/失败）
    print("get")      # 用户打开页面默认是一个GET请求，创建用户默认是一个POST提交请求
    # 通过判断用户请求的method方法判断用户是GET请求还是POST请求
    if request.method == "POST":
        try:
            print(request.POST)           # <QueryDict: {'name': ['dasdasdawd'], 'password': ['123456'], 'sex': ['0']}>
            # #方式一：一个一个获取值，然后一个一个入库，代码不优雅
            # name = request.POST.get('name',"")
            # password = request.POST.get('password',"")
            # sex = request.POST.get('sex',"")
            # print(name)
            # u = User()
            # u.name = name
            # u.password = password
            # u.sex = sex
            # u.save

            # #方式二：将提交的数据转为字典，一次性入库
            data = request.POST.dict()
            print(data)               # {'name': 'dasdasdawd', 'password': '123456', 'sex': '0'}
            User.objects.create(**data)
            msg = {"code": 0, "result": "添加用户成功"}
        except:
            msg = {"code": 1, "errmsg": "用户添加失败: %s" % traceback.format_exc()}
    # return的值，可以传递给前端模板进行渲染
    return render(request,"hello/useradd.html", {"msg":msg})


# 处理urls.py中定义用户查询功能的函数
def userlist(request):
    """
    用户列表 && 姓名搜索
    """
    # http://127.0.0.1:8001/?keyword=aaaa
    # 用户查询列表，就是一个get请求
    keyword = request.GET.get("keyword","")
    # 查询出所有的User表中的信息
    users = User.objects.all()
    # 如果用户传来的搜索关键字则对返回数据集进行过滤 --> 搜索功能
    if keyword:
        users = users.filter(name__icontains=keyword)
    print(users)   # 打印查询输出此表的返回Queryset列表，列表中的每个元素都为一个对象
    # 将查询出的所有的数据传入前端
    # return的值，可以传递给前端模板进行渲染
    return render(request, "hello/userlist.html",{"users":users,"keyword":keyword})

# 处理urls.py中定义用户更新功能的函数
from django.shortcuts import get_object_or_404
    # get_objects_or_404 是用来返回HTTP请求
    # 格式: get_objects_or_404(models, **kwargs)

def modify(request, **kwargs):
    """
    用户更新:
        1.通过ID拿到要更新的数据,并传到前端渲染
        2.将修改后的数据提交到后端
    """
    msg = {}
    print(kwargs)            # 获取devops/hello/urls.py中定义的 modify/(?P<pk>[0-9]+)?/'  所有的路由信息
    pk = kwargs.get("pk")    # pk就是devops/hello/urls.py中定义的 modify/(?P<pk>[0-9]+)?/'  即用户ID值   {'pk': '2'}

    # user = User.objects.get(pk=pk)         # 不严谨,用户ID不存在则报错
    user = get_object_or_404(User, pk=pk)  # 先查询用户传入的ID是否存在,如果存在则往下走,如果不存在则抛异常404

    # 提交更新过的数据到数据库
    if request.method == "POST":
        try:
            data = request.POST.dict()  # 获取到POST,并转换成字典
                                        # <QuerySet [<User: daizhe>, <User: mana>, <User: mana1>, <User: mana2>, <User: mana3>, <User: dasdasdawd>, <User: mana5>, <User: daizhe2>, <User: mana6>]>
            print(data)
            User.objects.filter(pk=pk).update(**data)  # 过滤出更新的字段并更新数据库
            msg = {"code": 0, "result": "更新用户成功"}
        # except Exception sa e:
        except:
            msg = {"code": 1, "errmsg": "更新用户失败: %s" % traceback.format_exc()}
            # msg = {"code": 1, "errmsg": "更新用户失败: %s" % e }
    # return的值，可以传递给前端模板进行渲染
    return render(request, "hello/modify.html", {"user":user, "msg":msg})

# 处理urls.py中定义用户删除功能的函数
from django.http import Http404
def userdel(request, **kwargs):
    """
    用户删除
    """
    msg = {}
    print(kwargs)           # 获取devops/hello/urls.py中定义的 userdel/(?P<pk>[0-9]+)?/'  所有的路由信息
    pk = kwargs.get("pk")   # pk就是devops/hello/urls.py中定义的 userdel/(?P<pk>[0-9]+)?/'  即用户ID值   {'pk': '2'}
    try:
        # 获取当前数据内容
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404

    #删除当前调数据
    if request.method == "POST":
        try:
            User.objects.get(pk=pk).delete()    # 根据提交的POST请求中的获取的用户ID进行删除
            msg = {"code": 0, "result": "删除用户成功"}
        except:
            msg = {"code": 1, "errmsg": "删除用户失败: %s" % traceback.format_exc()}
    # return的值，可以传递给前端模板进行渲染
    return render(request, "hello/userdel.html", {"user": user, "msg": msg})

