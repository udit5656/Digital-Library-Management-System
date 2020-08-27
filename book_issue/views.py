from django.apps import apps
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import BookIssueCode, IssuedBook
from .forms import AdminBookIssueCodeForm

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


@permission_required('book_issue.add_bookissuecode')
def admin_site_view(request):
    pending_book_issue_requests = BookIssueCode.objects.all().order_by('-created')
    if request.method == 'POST':
        form = AdminBookIssueCodeForm(request.POST)
        if form.is_valid():
            pk = request.POST.get('enter')
            book_issue_code = BookIssueCode.objects.get(pk=pk)
            if book_issue_code.check_code(form.cleaned_data['code']):
                issued_book = IssuedBook.create(user=request.user, book=book_issue_code.book)
                issued_book.save()
                book_issue_code.delete()
                return HttpResponseRedirect(reverse('book_issue:admin_site'))
            form.add_error('code', ValidationError("Wrong Code"))
        return render(request, 'book_issue/admin_issue.html',
                      {'form': form, 'pending_book_issue_requests': pending_book_issue_requests})
    form = AdminBookIssueCodeForm()
    context = {'pending_book_issue_requests': pending_book_issue_requests, 'form': form}
    return render(request, 'book_issue/admin_issue.html', context)
