from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm


def profile(request):
    user = request.user
    count = user.mypost.filter(user_id=user.id).count()
    print(count)
    return render(request, 'account/profile.html', {'user': user, 'mypost_count': count})


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
