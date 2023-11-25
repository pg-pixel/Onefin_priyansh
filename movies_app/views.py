from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache


from .models import Collection, Movie, GenreCount
from users_app.models import User
from .serializers import CollectionSerializer, MovieSerializer, GenreCountSerializer

from .Logic import call_api, validate_token, add_component


# Create your views here.
class MovieView(APIView):
    def get(self, request):
        """
        GET Request method for calling 3rd party API
        """
        
        # validate user
        token = request.COOKIES.get('jwt_token') 
        user = validate_token.Validate_token.validate_token(token)
        
        # fetch data from 3rd party API
        data = call_api.Api_call.api_call()

        # return response
        return Response(data, status=status.HTTP_200_OK)
        
class CollectionListView(APIView):
    def get(self, request):
        # validate token
        token = request.COOKIES.get('jwt_token') 
        user = validate_token.Validate_token.validate_token(token) 
        
        collections = Collection.objects.filter(user = user.id) 
        
        # fetch fav genre
        fav_genres = (GenreCount.objects
                      .filter(user_id = user.id)
                      .order_by('-genre_count')
                      .values_list('genre_name', flat = True)[:3])
        
        data = {
            "collections" : CollectionSerializer(collections, many = True).data, 
            "favorite_genres" : ", ".join([genre for genre in fav_genres])
        }
        
        return Response({
            "is_success": True, 
            "data": data
        })
     
    def post(self, request):
        # validate the request
        token = request.COOKIES.get('jwt_token') 
        user = validate_token.Validate_token.validate_token(token)
        
        # collect collection information
        data = request.data 
        try:
            collection_data = {
                "title": data["title"],
                "description": data["description"],
                "user": user.id
            }
        except Exception as exp:
            return Response({"message": "Bad Request"}, status = 400)
        
        result, status_code = add_component.Add_component.add_new_collection(user, data, collection_data)
        
        return Response(result, status = status_code)
        
class CollectionDetailsView(APIView):
    def get(self, request, collection_uuid):
        # validate token
        token = request.COOKIES.get('jwt_token') 
        user = validate_token.Validate_token.validate_token(token) 
        
        # fetch colection
        collection = Collection.objects.filter(id = collection_uuid).first()
        if not collection:
            return Response({"message": "collection uuid invalid"}, status = 400)
        
        data = CollectionSerializer(collection).data
        
        movies = Movie.objects.filter(collection = collection)
    
        data["movies"] = MovieSerializer(movies, many=True).data
        
        return Response(data)
    
    def put(self, request, collection_uuid):
        # validate token
        token = request.COOKIES.get('jwt_token') 
        user = validate_token.Validate_token.validate_token(token) 
        
        data = request.data 
        
        # fetch colection
        collection = Collection.objects.filter(id = collection_uuid).first()
        if not collection:
            return Response({"message": "collection uuid invalid"}, status = 400)
        
        collection_data = {
            "title": data.get("title", collection.title),
            "description": data.get("description", collection.description),
            "user": user.id
        } 
        
        result, status_code = add_component.Add_component.update_collection(user, data, collection_data, collection)

        return Response(result, status = status_code) 
    
    def delete(self, request, collection_uuid):
        # validate request
        token = request.COOKIES.get('jwt_token') 
        user = validate_token.Validate_token.validate_token(token) 
        
        collection = Collection.objects.filter(id = collection_uuid).first()
        if not collection:
            return Response({"message": "collection uuid invalid"}, status = 400)
        
        # reduce count of genre_count for a particular user id 
        collection = Collection.objects.get(id=collection_uuid)
        movie = Movie.objects.filter(collection = collection) 
        for movie_info in  MovieSerializer(movies, many=True).data:
            for genre_name in movie_info["genre"].split(','):
                genrecount = GenreCount.object.filter(user_id = user.id, genre_name = genre_name) 
                genrecount.genre_count -=1 
                genrecount.save()
                
        # delete the collection
        Collection.objects.get(id=collection_uuid).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RequestCountView(APIView):
    def get(self, request):
        cache_key = 'request_count'
        request_count = cache.get(cache_key, 0)
    
        return Response({"requests": request_count}) 
    
    def post(self, request):
        cache_key = 'request_count'
        cache.set(cache_key, 0)
    
        return Response({"message": "Request count reset successfully"})