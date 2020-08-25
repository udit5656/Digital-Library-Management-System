from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    PROGRAMME_STATES = (('Btech', 'Btech'),
                        ('Mtech', 'Mtech'),
                        ('Phd', 'Phd'))

    name = forms.CharField(max_length=20)
    roll_no = forms.IntegerField()
    year = forms.IntegerField()
    branch = forms.CharField(max_length=5)
    programme = forms.CharField(label="Enter your programme", widget=forms.Select(choices=PROGRAMME_STATES))
    email_id = forms.EmailField()
    gender = forms.CharField(max_length=6)
    profile_photo = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('name', 'gender', 'roll_no', 'branch', 'year', 'programme', 'email_id','profile_photo')
