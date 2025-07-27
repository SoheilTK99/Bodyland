from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages



def login_View(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('/home/')
        else:
            return render(request, 'account/login.html', {'error': 'نام کاربری یا رمز اشتباه است'})
    return render(request, 'account/login.html')




def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'رمز عبورها یکسان نیستند.')
            return render(request, 'account/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلاً ثبت شده.')
            return render(request, 'account/signup.html')

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)  # بعد از ساخت، واردش کن
        return redirect('/home/')  # تغییر بده به مسیر اصلی خودت

    return render(request, 'account/signup.html')


def logout_view(request):
    logout(request)
    return redirect('/home/')