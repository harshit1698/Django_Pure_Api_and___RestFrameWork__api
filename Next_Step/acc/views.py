from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode=api_settings.JWT_ENCODE_HANDLER

class Auth(APIView):
    permission_classes = [permissions.AllowAny]
    # data={'username'}


    def post(self,request,*args,**kwargs):
        print(request.user)
        data= request.data
        user=data.get('username')
        pwd=data.get('password')
        user = authenticate(username=user,password=pwd)
        payload=jwt_payload_handler(user)
        token=jwt_encode(payload)
        print(user)
        return Response({'token':token})

