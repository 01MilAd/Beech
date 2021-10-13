from rest_framework import serializers

from profiles.models import Profile
from story.models import Story


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'user', 'title', 'sound', 'cover', 'caption', 'created']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
