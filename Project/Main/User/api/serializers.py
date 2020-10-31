from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

        def save(self):
            user = User(
                email = self.validated_data['email'],
                username = self.validated_data['username']
            )
            password = self.validated_data['password'],

            user.save()
            return user
