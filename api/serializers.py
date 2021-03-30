from .models import *
from rest_framework import serializers

class PorfolioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Porfolio
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'