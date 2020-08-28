from django.urls import path

from . import views

app_name = 'librarian'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_view, name='search'),
    path('search/<str:q>/', views.book_issue_request_search_view, name='search_result'),
    path('issued-books/',views.issued_books_view,name='issued_books'),
]
