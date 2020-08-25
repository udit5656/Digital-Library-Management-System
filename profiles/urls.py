from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('<int:user_roll_no>/', views.profile_view, name='profile'),
    path('<int:user_roll_no>/edit', views.edit_profile, name='edit_profile')
]
