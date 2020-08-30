from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BookIssueCodeForm, SearchForm
from .tables import IssuedBooksTable

BookIssueCode = apps.get_model('book_issue', 'BookIssueCode')
IssuedBook = apps.get_model('book_issue', 'IssuedBook')


# Create your views here.
@permission_required('book_issue.add_bookissuecode')
def home(request):
    book_issue_requests = BookIssueCode.objects.all().order_by('-created')

    if request.method == 'POST':
        book_issue_code_form = BookIssueCodeForm(request.POST)
        search_form = SearchForm()
        if book_issue_code_form.is_valid():
            pk = request.POST.get('check_code')
            book_issue_code = BookIssueCode.objects.get(pk=pk)

            if book_issue_code.check_code(book_issue_code_form.cleaned_data['code']):
                issued_book = book_issue_code.issue_book()
                issued_book.add_deadline()
                messages.add_message(request, messages.INFO, 'Book Issued Successfully')
                return HttpResponseRedirect(reverse('librarian:home'))

            book_issue_code_form.add_error('code', ValidationError("Wrong Code"))
        context = {'book_issue_code_form': book_issue_code_form, 'book_issue_requests': book_issue_requests,
                   'search_form': search_form}

        return render(request, 'librarian/home.html', context)

    search_form = SearchForm(request.GET or None)
    book_issue_code_form = BookIssueCodeForm()

    if search_form.is_valid():
        q = search_form.cleaned_data['username']
        return HttpResponseRedirect(reverse('librarian:search_result', kwargs={'q': q}))

    context = {'book_issue_requests': book_issue_requests, 'book_issue_code_form': book_issue_code_form,
               'search_form': search_form}
    return render(request, 'librarian/home.html', context)


def search_view(request):
    search_form = SearchForm(request.GET or None)

    if search_form.is_valid():
        q = search_form.cleaned_data['username']
        return HttpResponseRedirect(reverse('librarian:search_result', kwargs={'q': q}))


def book_issue_request_search_view(request, q):
    user = User.objects.get(username=q)
    book_issue_requests = BookIssueCode.objects.all().filter(user=user).order_by('-created')
    search_form = SearchForm()
    if request.method == 'POST':
        book_issue_code_form = BookIssueCodeForm(request.POST)

        if book_issue_code_form.is_valid():
            pk = request.POST.get('check_code')
            book_issue_code = BookIssueCode.objects.get(pk=pk)

            if book_issue_code.check_code(book_issue_code_form.cleaned_data['code']):
                book_issue_code.issue_book()
                return HttpResponseRedirect(reverse('librarian:home'))

            book_issue_code_form.add_error('code', ValidationError("Wrong Code"))
        context = {'book_issue_code_form': book_issue_code_form, 'book_issue_requests': book_issue_requests,
                   'search_form': search_form}

        return render(request, 'librarian/search_result.html', context)

    book_issue_code_form = BookIssueCodeForm()
    context = {'book_issue_requests': book_issue_requests, 'book_issue_code_form': book_issue_code_form,
               'search_form': search_form}
    return render(request, 'librarian/search_result.html', context)


def issued_books_view(request):
    issued_books = IssuedBook.objects.all().order_by('-created')
    table = IssuedBooksTable(issued_books)
    context = {'issued_books': issued_books, 'table': table}
    return render(request, 'librarian/issued_books.html', context)
