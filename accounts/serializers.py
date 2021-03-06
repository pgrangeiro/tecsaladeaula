from rest_framework import serializers
from django.contrib.auth import get_user_model


class TimtecUserSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='get_full_name')
    picture = serializers.Field(source='get_picture_url')

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'name', 'email', 'first_name', 'last_name', 'biography', 'picture',)
