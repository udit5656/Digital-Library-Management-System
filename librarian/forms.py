from django import forms


class BookIssueCodeForm(forms.Form):
    code = forms.CharField(max_length=6, widget=forms.TextInput({'placeholder': 'Enter Code'}))


class SearchForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput({'placeholder': 'Search User'}))
