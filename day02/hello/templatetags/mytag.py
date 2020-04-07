from django import template    #导入模板类

register = template.Library()  #对模板进行注册

@register.filter               #用于模板过滤
def test(x,y):               # 接收三个参数
    return int(x)*2+int(y)