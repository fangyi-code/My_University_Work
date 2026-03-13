from django.http import JsonResponse
# django.contrib.auth:Django内置的用户认证系统
from django.contrib.auth import authenticate,login,logout

def signin(request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    user = authenticate(username = userName,password = passWord)

    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request,user)
                request.session['usertype'] = 'mgr'
                return JsonResponse({'ret':0})
            else:
                return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
        else:
            return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})

def signout(request):
    logout(request)
    return JsonResponse({'ret':0})