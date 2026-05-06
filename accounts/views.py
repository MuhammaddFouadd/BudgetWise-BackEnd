from rest_framework import viewsets, permissions, status, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login
from .models import *
from accounts.serializers import *

class AuthViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.AllowAny]

   def perform_create(self, serializer):
      """
        Overrides the default create behavior to use the custom
        create_user method (which handles password hashing).
      """
      User.objects.create_user(**serializer.validated_data)
   
   @action(detail=False, methods=['post'])
   def login(self ,request) :
      """
        Custom action for user login.
      """
      email = request.data.get('email')
      password = request.data.get('password')
      
      user = authenticate(request, username=email, password=password)      
      if user is not None:
         login(request, user)
         return Response ({"message": "Login successful"}, status= status.HTTP_200_OK)

      return Response ({"message": "Invlaid credentials"}, status= status.HTTP_401_UNAUTHORIZED)

