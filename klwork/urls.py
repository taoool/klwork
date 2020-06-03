"""klwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from klzg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', views.index),  # 首页
    path('salesman/', views.salesman),  # 业务员详情表
    path('customer_inf/', views.customer_inf),  # 客户详情表
    path('customer/', views.customer),  # 客户收款表
    path('project/', views.project),  # 支付项目表
    path('pay/', views.pay),  # 提成表
    path('finish/', views.finish),  # 付款记录表
    path('department/', views.department),  # 部门表

    path('add_customer/', views.add_customer),  # 增
    path('add_customer_inf/', views.add_customer_inf),
    path('add_salesman/', views.add_salesman),
    path('add_project/', views.add_project),
    path('add_pay/', views.add_pay),
    path('add_finish/', views.add_finish),
    path('add_department/', views.add_department),

    re_path('^modify_customer/(?P<cus_id>\d+)/$', views.modify_customer),  # 改
    re_path('^modify_customer_inf/(?P<cus_id>\d+)/$', views.modify_customer_inf),
    re_path('^modify_salesman/(?P<cus_id>\d+)/$', views.modify_salesman),
    re_path('^modify_project/(?P<cus_id>\d+)/$', views.modify_project),
    re_path('^modify_pay/(?P<cus_id>\d+)/$', views.modify_pay),
    re_path('^modify_finish/(?P<cus_id>\d+)/$', views.modify_finish),
    re_path('^modify_department/(?P<cus_id>\d+)/$', views.modify_department),

    re_path('delete_customer_inf/(?P<cus_id>\d+)/$', views.delete_customer_inf),  # 删
    re_path('delete_customer/(?P<cus_id>\d+)/$', views.delete_customer),
    re_path('delete_salesman/(?P<cus_id>\d+)/$', views.delete_salesman),
    re_path('delete_project/(?P<cus_id>\d+)/$', views.delete_project),
    re_path('delete_pay/(?P<cus_id>\d+)/$', views.delete_pay),
    re_path('delete_finish/(?P<cus_id>\d+)/$', views.delete_finish),
    re_path('delete_department/(?P<cus_id>\d+)/$', views.delete_department),




    path('123/', views.aba),  # 测试用
]
