from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
app_name='front'
def index(request):
    # ?username=xxx
    username=request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        return redirect('/login/')

def login(request):
    return HttpResponse('前台登录页面')
