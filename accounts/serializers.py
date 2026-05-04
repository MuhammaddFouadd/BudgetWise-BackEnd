"""
User serializer module for converting models' instances to/from JSON.

This module provides serialization and deserialization of User objects,
handling password hashing and field-level access control.
"""
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
   """
   Serializer for the User model.
   
   Handles conversion between User model instances and JSON representations,
   with special handling for password fields (write-only) and user creation.
   """
   class Meta:
      model = User
      fields = ['id', 'email', 'first_name', 'last_name', 'currency', 'password']

      # Field Options Overriding and Data acess control
      extra_kwargs ={
         'password':{'write-only':True},
      }
   
   def create (self, validated_data):
      return User.objects.create_user(**validated_data)