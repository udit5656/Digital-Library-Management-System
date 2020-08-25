from django.apps import apps
from django.shortcuts import render
from .models import BookIssueCode

Book = apps.get_model('books', 'Book')


# Create your views here.
def issue(request, book_id):
    book_issue_code = BookIssueCode.create(user=request.user, book=Book.objects.get(pk=book_id))
    book_issue_code.save()
    context = {'book_issue_code': book_issue_code}
    return render(request, 'book_issue/issue.html', context)
