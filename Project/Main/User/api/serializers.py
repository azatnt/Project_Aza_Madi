from rest_framework import serializers
from django.contrib.auth.models import User
from User.models import Profile
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response




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



class UserPasswordChangeSerializer(serializers.ModelSerializer):
    # old_password = serializers.CharField(required=True, max_length=30)
    # password = serializers.CharField(required=True, max_length=30)
    # confirmed_password = serializers.CharField(required=True, max_length=30)
    # image = serializers.FileField(source="profile.image", required = )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }



    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.username = validated_data['username']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        # instance.profile.image = validated_data['image']
        instance.email = validated_data['email']
        instance.save()
        print(instance.profile.image)
        return instance

    def create(self, validated_data):
        pass
    #
    # @property
    # def data(self):
    #     return {'Successfully changed': data}

        return Response(data)
