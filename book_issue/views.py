from django.apps import apps
from django.shortcuts import render

from .models import BookIssueCode

Book = apps.get_model('books', 'Book')


# Create your views here.
def issue(request, book_id):
    book = Book.objects.get(pk=book_id)
    if book.check_availability():
        book_issue_code = BookIssueCode.create(user=request.user, book=book)
        book_issue_code.save()
        book.books_available = book.books_available - 1
        book.save()
        context = {'error': None, 'book_id': book_id, 'book_issue_code': book_issue_code}
    else:
        error = "This book is currently not available. Please try later."
        context = {'error': error, 'book_id': book_id, 'book_issue_code': None}
    return render(request, 'book_issue/issue.html', context)

