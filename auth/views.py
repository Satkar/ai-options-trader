from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MongoUser
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request):
        user = MongoUser.objects(username=request.data['username']).first()
        if user and user.check_password(request.data['password']):
            token = RefreshToken.for_user(user)
            return Response({'access': str(token.access_token), 'refresh': str(token)})
        return Response({'error': 'Invalid credentials'}, status=401)