from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({'token': response.data['token']})