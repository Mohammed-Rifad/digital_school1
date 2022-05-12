from multiprocessing import managers
from xmlrpc.client import ResponseError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TeacherSerializer
from .models import *

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@api_view(['POST'])
 
def teacher_auth(request):
    
    print('llllllllllllllllllll')
    params=request.data
    statusCode=0
    email=params['email']
    passwd=params['passwd']
    print(email,passwd)
    try:
        login_check=Teacher.objects.get(email=email,password=passwd)
        print('00000000000000000000000',login_check)
        statusCode=200
        print('heeererrer')
    except:
        statusCode=401
        return Response({'statusCode':statusCode})
    return Response({'statusCode':statusCode})

@api_view(['GET'])
def view_teachers(request):
    
    teachers=Teacher.objects.all()
    ser=TeacherSerializer(teachers,many=True)
    return Response(ser.data)