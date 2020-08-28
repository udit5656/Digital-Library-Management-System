from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    PROGRAMME_STATES = (('Btech', 'Btech'),
                        ('Mtech', 'Mtech'),
                        ('Phd', 'Phd'))

    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    roll_no = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Roll No'}))
    year = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Academic Year'}))
    branch = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Branch Code'}))
    programme = forms.CharField(label="Enter your programme", widget=forms.Select(choices=PROGRAMME_STATES))
    email_id = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    gender = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Gender'}))
    profile_photo = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('name', 'gender', 'roll_no', 'branch', 'year', 'programme', 'email_id', 'profile_photo')
