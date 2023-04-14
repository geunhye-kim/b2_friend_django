from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Profile
from .forms import ProfileForm


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
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'account/profile_edit.html', {'form': form})
