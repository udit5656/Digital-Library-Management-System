from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Profile
from .forms import ProfileForm
from .tables import BookIssueCodeTable, ReturnedBookTable, IssuedBookTable

BookIssueCode = apps.get_model('book_issue', 'BookIssueCode')
IssuedBook = apps.get_model('book_issue', 'IssuedBook')
BookReturn = apps.get_model('book_issue', 'BookReturn')


# Create your views here.

@login_required
def profile_view(request, user_roll_no):
    profile = Profile.objects.get(roll_no=user_roll_no)
    book_issue_requests = BookIssueCode.objects.all().filter(user=request.user).order_by('-created')
    issued_books = IssuedBook.objects.all().filter(user=request.user).order_by('-created')
    returned_books = BookReturn.objects.all().filter(user=request.user).order_by('-created')
    table = BookIssueCodeTable(book_issue_requests)
    issued_books_table = IssuedBookTable(issued_books)
    returned_books_table = ReturnedBookTable(returned_books)
    context = {'profile': profile, 'table': table, 'returned_books_table': returned_books_table,
               'issued_books_table': issued_books_table}
    return render(request, 'profiles/profile.html', context)


def edit_profile(request, user_roll_no):
    profile = Profile.objects.get(roll_no=user_roll_no)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        form.fields['roll_no'].disabled = True
        if form.is_valid():
            form.save()
            profile = Profile.objects.get(roll_no=user_roll_no)
            context = {'user_roll_no': form.cleaned_data['roll_no']}
            return HttpResponseRedirect(reverse('profiles:profile', kwargs=context))
        context = {'form': form, 'user_roll_no': user_roll_no, 'profile': profile}
        return render(request, 'profiles/edit_profile.html', context)
    form = ProfileForm(instance=request.user.profile)
    form.fields['roll_no'].disabled = True
    context = {'form': form, 'user_roll_no': user_roll_no, 'profile': profile}
    return render(request, 'profiles/edit_profile.html', context)
