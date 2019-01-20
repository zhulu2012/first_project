from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('cms首页')
def login(request):
    return HttpResponse('cms登录页面')

