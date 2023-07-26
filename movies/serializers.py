from rest_framework import serializers 
from .models import Movie,Post


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['id','owner','name','desc']



class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['comment']