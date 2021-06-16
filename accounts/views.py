from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib import auth
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
#from .forms import CustomuserChangeForm

# Create your views here.
def index(req):
    return render(req, 'index.html')

def signup(req):
    if req.method == "POST":
        if req.POST['password1'] == req.POST['password2']:
            user = User.objects.create_user(username = req.POST['username'], password = req.POST['password1'])
            auth.login(req, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect('../main')
        else:
            form = UserCreationForm
            return render(req, 'signup.html', {'form':form, 'error':'비밀번호가 일치하지 않습니다.'})
    else:
        form = UserCreationForm
        return render(req, 'signup.html', {'form':form})
        
def login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            auth.login(req, form.get_user())
            return redirect('../main')
        else:
            form = AuthenticationForm()
            return render(req, 'login.html', {'form':form, 'error':'가입하지 않은 아이디이거나, 잘못된 비밀번호입니다.'})
    else:
        form = AuthenticationForm()
        return render(req, 'login.html', {'form':form})

@require_POST
def logout(req):
    auth.logout(req)
    return redirect('../main')
    
@require_POST
def delete(req):
    if req.user.is_authenticated:
        req.user.delete()
        auth.logout(req)
    return redirect('../main')
 
@login_required
def update_password(req):
    if req.method=="POST":
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            user = form.save() #로그아웃됨
            update_session_auth_hash(req, user) #세션유지
            return redirect('../main')
    else:
        form = PasswordChangeForm(req.user)
        return render(req, 'update_password.html', {'form':form})

#
#회원정보수정
#
#@login_required
#def update(req):
#    if req.method=="POST":
#        form = CustomUserChangeForm(req.POST, instance=req.user)
#        if form.is_valid():
#            form.save()
#            return redirect('../main')
#    else:
#        form = CustomUserChangeForm(instance=req.user)
#    return render(req, 'update.html', {'form':form})
