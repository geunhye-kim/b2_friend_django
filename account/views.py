from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

def profile(request):
    profile = Profile.objects.first()
    return render(request, 'profile.html', {'profile': profile})

def profile_edit(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_edit.html', {'form': form})
