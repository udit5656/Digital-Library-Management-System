from django.apps import apps
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BookIssueCodeForm

BookIssueCode = apps.get_model('book_issue', 'BookIssueCode')
IssuedBook = apps.get_model('book_issue', 'IssuedBook')


# Create your views here.
@permission_required('book_issue.add_bookissuecode')
def home(request):
    book_issue_requests = BookIssueCode.objects.all().order_by('-created')
    if request.method == 'POST':
        form = BookIssueCodeForm(request.POST)
        if form.is_valid():
            pk = request.POST.get('check_code')
            book_issue_code = BookIssueCode.objects.get(pk=pk)
            if book_issue_code.check_code(form.cleaned_data['code']):
                issued_book = IssuedBook.create(user=request.user, book=book_issue_code.book)
                issued_book.save()
                book_issue_code.delete()
                return HttpResponseRedirect(reverse('librarian:home'))
            form.add_error('code', ValidationError("Wrong Code"))
        context = {'form': form, 'book_issue_requests': book_issue_requests}
        return render(request, 'librarian/home.html', context)
    form = BookIssueCodeForm()
    context = {'book_issue_requests': book_issue_requests, 'form': form}
    return render(request, 'librarian/home.html', context)
