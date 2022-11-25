from django.shortcuts import render
from django.http import HttpResponse
from user.create_userid import create_userid


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':
        print(request.POST)
        print(dir(request.POST))
        print(request.POST.get('uname'))
        print(request.POST.get('pwd'))
        new_userid = create_userid()
        return HttpResponse(f"登录成功{new_userid}")
