from django.urls import path

from . import views

app_name = 'librarian'
urlpatterns = [
    path('', views.home, name='home')
]
