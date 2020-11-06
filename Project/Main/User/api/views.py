from rest_framework import status
from rest_framework.response import Response
from User.api.serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token



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
