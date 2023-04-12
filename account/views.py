from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm
from django.http import HttpResponse

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, '../../b2_friend_django/templates/post/profile_list.html',  {'profiles': profiles})

# user = request.user.is_authenticated

def profile_detail(request):
    user=request.user.is_authenticated
    print(user)
    profile = Profile.objects.get(id = request.user.id)
    print(profile)
    if request.method == 'GET':
        return render(request, '../../b2_friend_django/templates/post/profile_detail.html', {'profile': profile})
# def profile_detail(request, pk):
#     profile = get_object_or_404(Profile, pk=pk)
#     return render(request, 'profile_detail.html', {'profile': profile})

def profile_new(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm()
    return render(request, '../../b2_friend_django/templates/post/profile_edit.html', {'form': form})

def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, '../../b2_friend_django/templates/post/profile_edit.html', {'form': form})
