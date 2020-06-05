# 导入模板
from django import template

# 必须同名
register = template.Library()

# 自定义过滤器(最多两个参数)
@register.filter()
def multi_fliter(x, y):

    return x * y


# 自定义标签(可传多个参数)
@register.simple_tag()
def multi_tag(x, y):

    return x * y