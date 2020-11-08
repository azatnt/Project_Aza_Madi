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


# class ChangeUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#
#         def save(self):
#             user.set_password(self.validated_data['password'])
#             user.save()
#             return user

class UserPasswordChangeSerializer(serializers.ModelSerializer):
    # old_password = serializers.CharField(required=True, max_length=30)
    # password = serializers.CharField(required=True, max_length=30)
    # confirmed_password = serializers.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    #
    # def validate(self, data):
    #     # add here additional check for password strength if needed
    #     if not self.context['request'].user.check_password(data.get('old_password')):
    #         raise serializers.ValidationError({'old_password': 'Wrong password.'})
    #
    #     if data.get('confirmed_password') != data.get('password'):
    #         raise serializers.ValidationError({'password': 'Password must be confirmed correctly.'})
    #
    #     return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    @property
    def data(self):
        return {'Success': True}
