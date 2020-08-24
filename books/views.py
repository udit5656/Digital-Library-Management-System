from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookSearchForm
from .models import Book


# Create your views here.
@login_required
def home(request):
    if request.method == 'GET':
        form = BookSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['q']
            profile = User.objects.get(username=request.user.username).profile
            result = Book.objects.all().filter(
                Q(title__icontains=query) | Q(author_name__icontains=query) | Q(publisher_name__icontains=query) | Q(
                    pub_year__icontains=query))
            context = {'result': result, 'profile': profile}
            return render(request, 'books/result.html', context)
        profile = User.objects.get(username=request.user.username).profile
        context = {'profile': profile, 'form': form}
        return render(request, 'books/home.html', context=context)


@login_required
def detail_view(request, book_id):
    book = Book.objects.get(pk=book_id)
    profile = User.objects.get(username=request.user.username).profile
    context = {'book': book, 'profile': profile}
    return render(request, 'books/detail_page.html', context)
