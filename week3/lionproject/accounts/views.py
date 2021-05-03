from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid(): #이미 존재하는 아이디를 입력했을 경우 오류 메세지를 보냄
            if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:    
                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'] )
                new_user.save()
                auth.login(request, new_user)
                return redirect('blog:home')
            else:
                return render(request, 'accounts/signup.html', {'error': '비밀번호와 비밀번호 확인이 다릅니다', 'form':form})
        else:
            return render(request, 'accounts/signup.html', {'form':form})
    else:
        form = SignupForm(request.POST)
        return render(request, 'accounts/signup.html', {'form':form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = auth.authenticate(request, username = username, password = pw)
            if user is not None:
                auth.login(request, user)
                return redirect('blog:home')
            else:
                return render(request, 'accounts/login.html', {'error':'ID나 Password를 잘못 입력하였습니다.', 'form':form})
        else:
            return render(request, 'accounts/login.html', {'form':form})
    else:
        form = LoginForm(request.POST)
        return render(request, 'accounts/login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('blog:home')


