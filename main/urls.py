from django.urls import path
from main.views import register, login_view, profile, teacher_filter_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('filter-teachers/', teacher_filter_view, name='teacher_filter'),
    path('profile/', profile, name='profile'),
]
