from django.shortcuts import render
from django.db import connection
from django.contrib.auth.hashers import make_password

from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import User
from accounts.serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
   serializer_class = UserSerializer
   permission_classes = [permissions.AllowAny]
   queryset = User.objects.raw("SELECT * FROM accounts_user")

   # ------------------------------------------------------------
   def create (self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)

      if serializer.is_valid():
         self.perform_create(serializer)

         return Response({"message": "User created successfully"},status=status.HTTP_201_CREATED)
      
      return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
   
   # ------------------------------------------------------------
   def perform_create(self, serializer):
      data = serializer.validated_data

      hashed_password = make_password(data.get('password'))

      query = """
            INSERT INTO accounts_user (email, password, first_name , last_name, currency, language, data_joined)
            VALUES (%s, %s, %s, %s, %s, %s, NOW())
            """
      
      params = [
         data.get('email'),
         data.get('password'),
         data.get('first_name', ''),
         data.get('last_name', ''),
         data.get('currency', 'EGP'),
         data.get('language', 'EG'),
      ]

      with connection.cursor() as cursor:
         cursor.execute(query,params)