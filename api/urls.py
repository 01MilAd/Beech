from rest_framework import routers

from api.views import StoryViewSet, ProfileViewSet

router = routers.SimpleRouter()
router.register('stories', StoryViewSet, basename='api_story')
router.register('profiles', ProfileViewSet, basename='api_profile')

