from django.shortcuts import render, redirect
import xlrd

# Create your views here.

xlsd = xlrd.open_workbook(r'C:\Users\12817\Desktop\新建文件夹\4月销量 - 副本.xlsx')