from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
@login_required
def home(request):
    profile = User.objects.get(username=request.user.username).profile
    context = {'profile': profile}
    return render(request, 'books/home.html', context=context)
