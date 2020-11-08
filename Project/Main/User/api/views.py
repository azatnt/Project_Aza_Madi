from rest_framework import status
from rest_framework.response import Response
from User.api.serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics


class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully added a new user'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


# class UpdateUser(generics.UpdateAPIView):
#
#     def get(self, request):
#         user = ChangeUserSerializer(request.user)
#         return Response(user.data)
#
#     def update(self, request, *args, **kwargs):
#         print(request.user)
#         user = request.user
#         user_serializer = ChangeUserSerializer(request.user, data=request.data, partial=True)
#         # user_serializer.is_valid(raise_exception=True)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             # user.set_password(user_serializer.data.get('password'))
#             # user.save()
#             print(user.password)
#             response = {'user': user_serializer.data}
#             return Response(response)
#         return Response({"message": "Didn't updated"})


class UpdateUser(generics.UpdateAPIView):
    serializer_class = UserPasswordChangeSerializer
    model = User
    # permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user
