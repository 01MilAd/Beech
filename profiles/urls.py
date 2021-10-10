from django.urls import path
from .views import *

app_name = 'profile'
urlpatterns = [
    path('profile/<int:pk>/', profile, name='profile'),
    path('add_profile/', add_profile, name='add_profile'),
    # path('create_profile/<int:user_id>/', create_profile, name='create_profile'),
    path('create_profile/<int:pk>/', CreateProfile.as_view(), name='create_profile'),
    path('edit_profile/<int:user_id>/', edit_profile, name='edit_profile'),
    # path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
]
