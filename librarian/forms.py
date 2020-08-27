from django import forms


class BookIssueCodeForm(forms.Form):
    code = forms.CharField(max_length=6)


class SearchForm(forms.Form):
    username = forms.CharField(max_length=30)
