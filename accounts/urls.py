from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('<int:user_roll_no>/', views.profile_view, name='profile'),
    path('<int:user_roll_no>/edit',views.edit_profile,name='edit_profile')
]
