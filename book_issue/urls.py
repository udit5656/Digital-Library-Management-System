from django.urls import path
from . import views

app_name = 'book_issue'
urlpatterns = [
    path('<int:book_id>/', views.issue, name='issue'),
    path('return/<int:book_issue_id>/', views.book_return, name='book_return'),
]
