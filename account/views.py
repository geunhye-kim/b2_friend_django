from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Profile


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
