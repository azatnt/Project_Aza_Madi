from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator



class RegisterSerializer(serializers.ModelSerializer):

        def save(self):
            user = User(
                email=self.validated_data['email'],
                username=self.validated_data['username'],
            )
            e_mail = self.validated_data['email']
            # password2 = self.validated_data['password2']
            if User.objects.filter(email=e_mail).count()>0:
                raise serializers.ValidationError({'email': 'User with that email already exists'})
            # if password != password2:
            #     raise serializers.ValidationError({'password' : 'Passwords must be the same'})
            user.set_password(self.validated_data['password'])
            user.save()
            return user

        email = serializers.EmailField()

        # validators=[UniqueValidator(queryset=User.objects.all())]
        # password2 = serializers.CharField(write_only=True),
        class Meta:
            model = User
            fields = ['username', 'email', 'password']
            extra_kwargs = {
                'password': {'write_only': True},
                'email': {'required': False}
            }
