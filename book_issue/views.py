from django.apps import apps
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import BookIssueCode, IssuedBook
from .forms import BookReturnCodeForm

Book = apps.get_model('books', 'Book')


# Create your views here.
def issue(request, book_id):
    book = Book.objects.get(pk=book_id)
    if IssuedBook.objects.all().filter(user=request.user).filter(book=book).count() > 0:
        error = "You already have issued this book"
    elif BookIssueCode.objects.all().filter(user=request.user).filter(book=book).count() > 0:
        error = "You already requested this book."
    elif BookIssueCode.objects.all().filter(user=request.user).count() >= 2:
        error = "You already have reached maximum book issue requests limit."
    elif book.check_availability():
        book_issue_code = BookIssueCode.create(user=request.user, book=book)
        book_issue_code.save()
        book.books_available = book.books_available - 1
        book.save()
        context = {'error': None, 'book_id': book_id, 'book_issue_code': book_issue_code}
        return render(request, 'book_issue/issue.html', context)
    else:
        error = "This book is currently not available. Please try later."

    context = {'error': error, 'book_id': book_id, 'book_issue_code': None}
    return render(request, 'book_issue/issue.html', context)


def book_return(request, book_issue_id):
    issued_book = IssuedBook.objects.get(pk=book_issue_id)
    if request.method == 'POST':
        form = BookReturnCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if issued_book.check_code(code=code):
                issued_book.return_book()
                return HttpResponseRedirect(
                    reverse('profiles:profile', kwargs={'user_roll_no': request.user.profile.roll_no}))
            code.add_error('code', ValidationError('Wrong Code'))
        context = {'form': form, 'issued_book': issued_book}
        return render(request, 'book_issue/return_book.html', context)

    form = BookReturnCodeForm()
    context = {'form': form, 'issued_book': issued_book}
    return render(request, 'book_issue/return_book.html', context)


def cancel_request(request, book_issue_request_id):
    book_issue_request = BookIssueCode.objects.get(pk=book_issue_request_id)
    book = Book.objects.get(pk=book_issue_request.book.pk)
    book.books_available += 1
    book.save()
    book_issue_request.delete()
    return HttpResponseRedirect(reverse('profiles:profile', kwargs={'user_roll_no': request.user.profile.roll_no}))
