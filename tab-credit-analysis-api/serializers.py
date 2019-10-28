# serializers.py

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = 'name'  # TODO add more fields
