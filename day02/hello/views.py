from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, QueryDict
from hello.models import User   #导入module

def userlist(request):
    users = User.objects.all()
    print(users)
    return render(request, 'hello/userlist.html', {'users':users})   #users为传递给前端template的K



#list user
# def list(request):
#     value = ['python', 'django', 'java']
#     users = [
#         {'username': 'kk1', 'name_cn': 'kk1', 'age': 18},
#         {'username': 'kk2', 'name_cn': 'kk2', 'age': 19},
#         {'username': 'kk3', 'name_cn': 'kk3', 'age': 20},
#     ]
#     print(users)
#     # return render(request,'hello/list.html',{'users':users})
#     return render(request,'hello/userlist.html',{'users':users, 'value':value})



#template渲染数据到html
# def index(request):
#     classname = "DevOps"                #普通变量
#     books = ['Python','Java','Django']  #列表
#     user = {'name':'kk','age':18}       #字典
#     # return render(request, "hello/hello.html")
#
#     # 普通变量：前端渲染的变量名称为testclass,定义好的变量为classname
#     # 列表 ： books，在前端templates，使用列表索引取值
#     # 字典 ： user， 在前端template，使用字典K/V取值
#     # return render(request, "hello/test.html",{'testclassname':classname,"books":books, "user":user})
#
#     # 列表中嵌套其他数据类型
#     userlist = [ {'name':'kk','age':18}, {'name':'rock','age':19},{'name':'mage','age':20}]
#     return render(request, 'hello/test.html', \
#                   {'classname': classname,"books":books,"user":user, "userlist":userlist })


# def index(request):
#     return HttpResponse("<p>Hello Word, Hello, Django</p>")

#1、普通url参数 http://127.0.0.1:8000/hello/?year=2019&month=06
# def index(request):
#     #设置默认值的方式获取数据更优雅
#    year = request.GET.get("year", "2019")
#     #直接获取数据，没有会报错，不建议
#    month = request.GET.get("month", "06")
#    return HttpResponse("year is %s,month is %s" % (year,month))

#2、位置传参的接收方法--> 函数种的参数和URL种的位置要对应，比较死板不推荐
#http://127.0.0.1:8001/hello/2019/06
# def index(request, year, month):
#     return HttpResponse("year is %s,month is %s" % (year, month))

#3、URL通过识别关键字传参数(?<参数名>参数类型)  --> 视图中直接通过参数名获取值（最常用）
# http://127.0.0.1:8001/hello/2019/06/
# def index(request, **kwargs):
#     print(kwargs)
#     year = kwargs.get("year")
#     month = kwargs.get("month")
#     return HttpResponse("year is %s,month is %s" % (year,month))

#另一种写法 --> 函数参数位置无关，以关键字为准，更加灵活
# def index(request, month, year):
#     return HttpResponse("year is %s,month is %s" % (year,month))

##########post请求传参数############
# 请求传参接收，默认为GET请求，通过method判断POST请求
# def index(request):
#     print(request.scheme)  # http
#     print(request.method)  # GET:获取资源/POST:输出实体本体/PUT：输出文件/HEAD：获取报文首部/DELETE：删除文件/OPTION：询问支持的方法/TRACE：追踪路径/CONNECT：要求用隧道协议连接代理/LINK：建立和资源之间的联系/UNLINK：断开连接关系
#     print(request.headers)  # {'Content-Length': '', 'Content-Type': 'text / plain', ……}
#     print(request.path)  # /hello/
#     print(request.META)  # {'REMOTE_ADDR': '1.119.56.6','HTTP_HOST': '123.56.73.115:8000', ……}
#     print(request.GET)  # <QueryDict: {'year': ['2019'], 'month':['06']} >: 获取相应信息中get发送的数据, request.GET.getlist('id'), 适⽤用于复选框的场景，如：id = 1 & id = 2, 结果存为列列表
#     data = request.GET
#     year = data.get("year", "2019")
#     month = data.get("month", "10")
#
#     #method请求方法为POST
#     if request.method == "POST":
#         print(request.method)  # POST
#     print(request.body)  # b'year=2019&month=06'
#     print(QueryDict(request.body).dict())
#     print(request.POST)  # <QueryDict: {'year': ['2019'],'month': ['06']} > 获取相应信息中post发送的数据,request.POST.getlist('id')
#     data = request.POST
#     year = data.get("year", "2018")
#     month = data.get("month", "07")
#     return HttpResponse("year is %s,month is %s" % (year, month))
