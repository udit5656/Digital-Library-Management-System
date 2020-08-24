from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:book_id>/', views.detail_view, name='detail_view')
]
