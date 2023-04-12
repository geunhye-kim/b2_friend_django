from django.urls import path
from . import views

# app_name = 'profiles'

urlpatterns = [
    # path('', views.profile_list, name='profile_list'),
    path('new/', views.profile_new, name='profile_new'),
    # path('<int:pk>/', views.profile_detail, name='profile_detail'),
    # path('<int:pk>/edit/', views.profile_edit, name='profile_edit'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]

