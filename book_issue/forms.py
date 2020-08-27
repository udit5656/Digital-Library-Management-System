from django import forms


class AdminBookIssueCodeForm(forms.Form):
    code = forms.CharField(max_length=6)
