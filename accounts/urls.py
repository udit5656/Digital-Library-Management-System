from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('login/admin-site', auth_views.LoginView.as_view(template_name='registration/admin_login.html'),
         name='admin_site_login'),
]
