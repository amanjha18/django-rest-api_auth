from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404 
from rest_framework import status 
from django.http import HttpResponse
from rest_framework.response import Response

from .serializers  import UserSerializer

class SignUp(APIView):
    def post(self, request):
        try:
            params=request.data
            try:
                password=params.pop('password')
            except:
                password=None
            if not password:
                content = {'status': False, 'message': 'oops password not found'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            params.update(password=password)
            try:
                serializer=UserSerializer(data=params)
                if serializer.is_valid(raise_exception=True): #show exact error using raise_excepion
                    user=serializer.save()
                    user.set_password(password)
                    user.save()
                    content = {'status': True, 'message': 'signup successfully', 'data': serializer.data}
                    return Response(content,status=status.HTTP_201_CREATED)
            except:
                content = {'status': False, 'message': 'oops, somthing went wrong', 'errors': serialzerer.errors}
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception:
            content = {"status":False,"message":"Something went wrong"}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



