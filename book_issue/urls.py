from django.urls import path
from . import views

app_name = 'book_issue'
urlpatterns = [
    path('<str:book_id>/', views.issue, name='issue'),
]