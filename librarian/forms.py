from django import forms


class BookIssueCodeForm(forms.Form):
    code = forms.CharField(max_length=6)
