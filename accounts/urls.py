from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),

]
