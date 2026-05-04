from rest_framework import serializers
from .models import User

class UserSerializer (serializers.ModelSerializer):
   class Meta:
      model = User
   fields = ['id', 'email', 'first_name', 'last_name', 'currency', 'password']   
   # Field Options Overriding and Data acess control
   extra_kwargs ={
      'password':{'write-only':True},
   }
   
   def create (self, validated_data):
      return User.objects.create_user(**validated_data)