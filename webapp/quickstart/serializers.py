from rest_framework import serializers
from .models import *

class studentserializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
