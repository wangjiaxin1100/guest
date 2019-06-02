from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    print ("get方法调用返回index页面")
    return render(request,"index.html")
    # return HttpResponse("HELLO DJANGO!")
# 登录操作
def login_action(request):
    if request.method == 'POST':
        # 判断post方法成功
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        if username == 'admin' and password == 'admin123':
            # return HttpResponseRedirect('/event_manage')
            response = HttpResponseRedirect('/event_manage')
            # response.set_cookie('user',username,3600) #浏览器Cookies
            request.session['user'] = username #将session信息记录在浏览器
            return response
            # return HttpResponse('Login success!')
        else:
            return render(request,'index.html',{'error':'username or password error!'})
#发布会管理
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user','')  #读取浏览器Cookies
    username = request.session.get('user','')
    return render(request,"event_manage.html")