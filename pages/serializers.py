# serializers.py
from rest_framework import serializers
from .models import User
from django.utils.translation import gettext as _

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # You can also specify individual fields if needed
