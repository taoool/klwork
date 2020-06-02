from django.shortcuts import render, redirect, HttpResponse
from klzg import models
# Create your views here.
def index(request):
    """导航页"""
    return render(request, "index.html")

def show(request):
    """总表"""
    tol = models.Pay.objects.all()
    ret = models.Pay.objects.all()
    return render(request, "show.html", locals())