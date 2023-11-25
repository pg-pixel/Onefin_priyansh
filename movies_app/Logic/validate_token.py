from users_app.models import User
import jwt
from rest_framework.exceptions import AuthenticationFailed

class Validate_token:
    @staticmethod
    def validate_token(token):
        
        if not token:
            raise AuthenticationFailed('Please Authenticate!(Not Authenticated)') 
        try:
            payload = jwt.decode(token, 'secret', algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Please Authenticate!(token Expired)') 
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        
        user = User.objects.get(id = payload['id']) 
        
        return user
        