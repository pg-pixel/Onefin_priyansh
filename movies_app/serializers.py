import uuid
from rest_framework import serializers
from . models import GenreCount, Movie, Collection

class GenreCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreCount  
        fields = ('genre_name', 'user_id')
        
class CollectionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True) 
    class Meta:
       model = Collection
       fields = ('id', 'title', 'description', 'user') 
       
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        
        return instance
        
       
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie 
        fields = ('title', 'description', 'genres', 'uuid') 
        
    def validate(self, data):
        allowed_fields = ('title', 'description', 'genres', 'uuid')
        if not set(data.keys()).issubset(set(allowed_fields)):
            raise serializers.ValidationError("Incorrect fields passed")
        
        return data
        
    def create(self, validated_data):
        
        return Movie.objects.create(**validated_data)