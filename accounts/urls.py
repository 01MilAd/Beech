from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('register/', views.user_register, name='register'),
    path('register/', views.register, name='register'),
]
