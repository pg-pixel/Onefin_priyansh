# import django based modules/packages
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
# general imports
import jwt
import datetime


# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True) 
        serializer.save() 
        
        return Response(serializer.data) 
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None) 
        
        user = User.objects.filter(email = email).first()
        
        if not user:
            raise AuthenticationFailed('User is not registered!') 
        
        if not user.check_password(password):
            raise AuthenticationFailed('Password is incorrect!') 
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response() 
        response.set_cookie(key = 'jwt_token', value = token, httponly = True)
        response.data = {
            'message': 'Login succesful'
        }
        
        return response
        
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt_token') 
        
        if not token:
            raise AuthenticationFailed('Please Authenticate!(Not Authenticated)') 
        try:
            payload = jwt.decode(token, 'secret', algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Please Authenticate!(token Expired)') 
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
            
        user = User.objects.get(id = payload['id'])
        serializer = UserSerializer(user) 
        
        return Response(serializer.data)