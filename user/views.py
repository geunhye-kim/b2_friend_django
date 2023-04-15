from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserModel
from django.contrib.auth import get_user_model  # 사용자가 있는지 검사하는 함수
from django.contrib import auth  # 사용자 auth 기능
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# SIGN UP - user_name, user_password, user_email, user_number, user_address, user_bio
def signup_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 로그인 된 사용자가 요청하는지 검사
        if user:  # 로그인이 되어있다면
            return redirect('/feed')
        else:  # 로그인이 되어있지 않다면
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        user_password = request.POST.get('user_password', '')
        user_password2 = request.POST.get('user_password2', '')
        user_email = request.POST.get('user_email', '')
        user_number = request.POST.get('user_number', 'None')
        user_address = request.POST.get('user_address', '')
        user_bio = request.POST.get('user_bio', '')

        if user_password != user_password2:
            # 패스워드가 같지 않다고 알람
            return render(request, 'user/signup.html', {'error': '비밀번호를 확인해 주세요!'})
        else:
            if user_name == '' or user_password == '':
                return render(request, 'user/signup.html', {'error': '아이디와 비밀번호는 필수입니다.'})

            exist_user = get_user_model().objects.filter(username=user_name)
            if exist_user:
                # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
                return render(request, 'user/signup.html', {'error': '이미 이용중인 아이디입니다..'})
            else:
                UserModel.objects.create_user(username=user_name, password=user_password, email=user_email,
                                              phone=user_number, address=user_address, bio=user_bio)
                return redirect('/login')  # 회원가입이 완료되었으므로 로그인 페이지로 이동


# SIGN IN
def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        user_password = request.POST.get('user_password', '')

        if user_name == '' or user_password == '':
            return render(request, 'user/login.html', {'error': '아이디와 비밀번호는 필수입니다.'})
        else:
            me = auth.authenticate(
                request, username=user_name, password=user_password)  # 사용자 불러오기
            if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
                auth.login(request, me)
                return redirect('/')
            else:
                # 로그인 실패
                return render(request, 'user/login.html', {'error': '유저이름 혹은 패스워드를 확인 해 주세요.'})

    elif request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인 되어 있는지 검사
        if user:  # 로그인이 되어 있다면
            return redirect('/')
        else:  # 로그인이 되어 있지 않다면
            return render(request, 'user/login.html')


@login_required
def logout_view(request):
    auth.logout(request)  # 인증 되어있는 정보를 없애기
    return redirect("/")


def profile(request):
    if request.method == 'GET':
        user = request.user
        count = user.mypost.filter(user_id=user.id).count()
        post = user.mypost.filter(user_id=user.id)
        paginator = Paginator(post, per_page=8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'account/profile.html', {'user': user, 'mypost_count': count, 'page_obj': page_obj})


def profile_edit(request):
    if request.method == 'GET':
        user = request.user
        return render(request, 'account/profile_edit.html', {'user': user})
    elif request.method == 'POST':
        user = request.user
        user.username = request.POST.get('name', '')
        user.phone = request.POST.get('number', '')
        user.email = request.POST.get('email', '')
        user.bio = request.POST.get('bio', '')
        user.save()
        return redirect('profile')
