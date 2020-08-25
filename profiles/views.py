from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Profile
from .forms import ProfileForm


# Create your views here.

@login_required
def profile_view(request, user_roll_no):
    profile = Profile.objects.get(roll_no=user_roll_no)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)


def edit_profile(request, user_roll_no):
    profile = Profile.objects.get(roll_no=user_roll_no)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            profile = Profile.objects.get(roll_no=user_roll_no)
            context = {'user_roll_no': form.cleaned_data['roll_no']}
            return HttpResponseRedirect(reverse('profiles:profile', kwargs=context))
        context = {'form': form, 'user_roll_no': user_roll_no, 'profile': profile}
        return render(request, 'profiles/edit_profile.html', context)
    form = ProfileForm(instance=request.user.profile)
    context = {'form': form, 'user_roll_no': user_roll_no, 'profile': profile}
    return render(request, 'profiles/edit_profile.html', context)
