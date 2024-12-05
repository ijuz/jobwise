import requests
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from . serializer import SignupSerializer
from .models import CustomUser



@api_view(['POST'])
@permission_classes([AllowAny])
def SignUp(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.is_workker = True
        user.save()
        refresh = RefreshToken.for_user(user)
        tokens = {
                "access": str(refresh.access_token),
                "refresh":str(refresh)
        }
        return Response({
            "status":"6000",
            "message": "User registered successfully.",
            "tokens":tokens
        }, status=status.HTTP_201_CREATED)
    return Response({
        "error": "Validation failed.",
        "details": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)