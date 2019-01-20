from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def book_list(request):
    return HttpResponse("首页")


def book(request,book_id):
    text="你获取的图书ID是：%s"% book_id
    return HttpResponse(text)

def author(request):
    author_id =request.GET.get("id")
    text= "作者的ID是：%s"% author_id
    return HttpResponse(text)


