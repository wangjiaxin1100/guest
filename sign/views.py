from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
# def index(request):
    # return render(request,"index.html")
    # return HttpResponse("HELLO DJANGO!")

def login_action(request):
    if request.method=="GET":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username , password=password)
        if user is not None:
            auth.login(request,user)
        # if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookies('user',username,3600)
            request.session['user'] = username
            return response
            # return HttpResponse('login success!')
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
@login_required
def event_manage(request):
    # username = request.Cookies.get('user','')
    username = request.session.get('user','')
    return render(request,"event_manage.html",{"user":username})