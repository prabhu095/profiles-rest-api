from rest_framework import  serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    # The way we work with model serializers is we create meta class
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,   # As password is a sensitive field we want write only
                'style': {'input_type': 'password'}

            }
            # Create user function => Password gets hashed
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )

        return user
