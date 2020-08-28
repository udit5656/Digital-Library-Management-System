from django import forms


class BookReturnCodeForm(forms.Form):
    code = forms.CharField(max_length=6, widget=forms.TextInput({'placeholder': 'Enter Code'}))
