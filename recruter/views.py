from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated  # Require authentication
from . serializer import JobPostingSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def create_job(request):
    serializer = JobPostingSerializer(data=request.data, context={'request': request})
    
    if serializer.is_valid():
        serializer.save() 
        return Response({
            "status": "success",
            "message": "Job posted successfully.",
            "job_posting": serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response({
        "status": "error",
        "message": "Validation failed.",
        "details": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
