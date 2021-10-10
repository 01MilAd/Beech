from django.urls import path
from .views import *

app_name = 'story'
urlpatterns = [
    # path('', home, name='home'),
    path('', Home.as_view(), name='home'),
    # path('all_story/', all_story, name='all_story'),
    path('all_story/', AllStory.as_view(), name='all_story'),
    path('create_story/', create_story, name='create_story'),
    # path('create_story/', CreateStory.as_view(), name='create_story'),
    # path('edit_story/<int:user_id>/<int:story_id>/', edit_story, name='edit_story'),
    path('edit_story/<int:pk>/', EditStory.as_view(), name='edit_story'),
    # path('delete_story/<int:user_id>/<int:story_id>/', delete_story, name='delete_story'),
    path('delete_story/<int:pk>/', DeleteStory.as_view(), name='delete_story'),
]
