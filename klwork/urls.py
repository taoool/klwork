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
import excel.views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', views.index),  # 首页
    path('salesman/', views.salesman),  # 业务员详情表
    path('customer_inf/', views.customer_inf),  # 客户详情表
    path('customer/', views.customer),  # 客户收款表
    path('project/', views.project),  # 支付项目表
    path('commission/', views.commission),  # 提成表
    # re_path('commission/(?P<customer_name>[\u4E00-\u9FA5]+)/$', views.commission_detail),  # 提成详情
    re_path('commission/(?P<customer_name>.*[\u4E00-\u9FA5]+)/$', views.commission_detail),  # 提成详情
    # path('finish/', views.finish),  # 付款记录表
    path('sales/', views.sales),  # 销量表
    path('department/', views.department),  # 部门表

    path('history/', excel.views.history),  # 历史记录


    path('modify_customer/', views.modify_customer),  # 增
    path('modify_customer_inf/', views.modify_customer_inf),
    path('modify_salesman/', views.modify_salesman),
    path('modify_project/', views.modify_project),
    path('modify_commission/', views.modify_commission),
    re_path('add_commission_detail/(?P<customer_name>.*[\u4E00-\u9FA5]+)/$', views.add_commission_detail),
    path('modify_finish/', views.modify_finish),
    path('modify_department/', views.modify_department),

    re_path('^modify_customer/(?P<cus_id>\d+)/$', views.modify_customer),  # 改
    re_path('^modify_customer_inf/(?P<cus_id>\d+)/$', views.modify_customer_inf),
    re_path('^modify_salesman/(?P<cus_id>\d+)/$', views.modify_salesman),
    re_path('^modify_project/(?P<cus_id>\d+)/$', views.modify_project),
    re_path('^modify_commission/(?P<cus_id>\d+)/$', views.modify_commission),
    re_path('^modify_commission_detail/(?P<cus_id>\d+)/$', views.modify_commission_detail),
    re_path('^modify_finish/(?P<cus_id>\d+)/$', views.modify_finish),
    re_path('^modify_department/(?P<cus_id>\d+)/$', views.modify_department),
    re_path('^modify_sales/(?P<cus_id>\d+)/$', views.modify_sales),

    re_path('delete_customer_inf/(?P<cus_id>\d+)/$', views.delete_customer_inf),  # 删
    re_path('delete_customer/(?P<cus_id>\d+)/$', views.delete_customer),
    re_path('delete_salesman/(?P<cus_id>\d+)/$', views.delete_salesman),
    re_path('delete_project/(?P<cus_id>\d+)/$', views.delete_project),
    re_path('delete_commission/(?P<cus_id>\d+)/$', views.delete_commission),
    re_path('delete_commission_detail/(?P<cus_id>\d+)/$', views.delete_commission_detail),
    re_path('delete_finish/(?P<cus_id>\d+)/$', views.delete_finish),
    re_path('delete_department/(?P<cus_id>\d+)/$', views.delete_department),

    re_path('commission/(?P<time_id>\d+-\d{2})/$', views.commission),  # 日期筛选
    re_path('project/(?P<time_id>\d+-\d{2})/$', views.project),
    re_path('finish/(?P<time_id>\d+-\d{2})/$', views.finish),
    re_path('commission/(?P<year_id>\d{4})/$', views.commission),  # 年
    re_path('commission/(?P<year_on>\d{4})/(?P<month_id>\d{2})/$', views.commission),  # 月

    re_path('commission/(?P<customer_name>.*[\u4E00-\u9FA5]+)/(?P<year_id>\d{4})/$', views.commission_detail),  # 年
    re_path('commission/(?P<customer_name>.*[\u4E00-\u9FA5]+)/(?P<year_on>\d{4})/(?P<month_id>\d{2})/$', views.commission_detail),  # 月

    path('commission_flash/', views.commission_flash),  # 刷新
    # re_path('commission_flash_detail/(?P<cus_id>\d+)/$', views.commission_flash_detail),  # 刷新

    path ('history_out', excel.views.history_out),  # 导出


    path('123/', views.aba),  # 测试用
    re_path('123.*/(?P<year_id>\d{4})/$', views.aba),
    re_path('123.*/(?P<year_id>\d{4})/$', views.aba),
]
