from rest_framework import serializers
from .models import *

class TooDooSerializer(serializers.ModelSerializer):
    class Meta:
        model = TooDoo
        fields = ('id','title', 'description','date','status','place')