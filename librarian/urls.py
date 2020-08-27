from django.urls import path

from . import views

app_name = 'librarian'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_view, name='search'),
    path('search/<str:q>/', views.search_result_view, name='search_result'),
]
