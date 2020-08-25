from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.apps import apps
from profiles.forms import ProfileForm
Profile = apps.get_model('profiles', 'Profile')


def signup_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            name = profile_form.cleaned_data['name']
            roll_no = profile_form.cleaned_data['roll_no']
            gender = profile_form.cleaned_data['gender']
            branch = profile_form.cleaned_data['branch']
            year = profile_form.cleaned_data['year']
            programme = profile_form.cleaned_data['programme']
            email_id = profile_form.cleaned_data['email_id']
            profile_photo = profile_form.cleaned_data['profile_photo']
            profile = Profile.objects.create(user=user, name=name, roll_no=roll_no, gender=gender, year=year,
                                             branch=branch,
                                             programme=programme, email_id=email_id, profile_photo=profile_photo)
            profile.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('books:home'))
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'accounts/signup.html', context)
    user_form = UserCreationForm()
    profile_form = ProfileForm()
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'accounts/signup.html', context)
