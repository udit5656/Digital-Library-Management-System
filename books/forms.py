from django import forms


class BookSearchForm(forms.Form):
    q = forms.CharField(max_length='100', label='Search Book')
