from rest_framework import serializers
from .models import users

class usersSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = '__all__'
