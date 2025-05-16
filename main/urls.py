from django.urls import path
from main.views import register, login_view, profile, teacher_filter_view, home_view, teacher_detail_view, take_slot_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('filter-teachers/', teacher_filter_view, name='teacher_filter'),
    path('profile/', profile, name='profile'),
    path('teacher/<int:teacher_id>/', teacher_detail_view, name='teacher_detail'),
    path('teacher/<int:teacher_id>/slot/<int:slot_id>/take/', take_slot_view, name='take_slot'),
]
