from users_app.models import User 
from movies_app.models import Collection, Movie, GenreCount 

from movies_app.serializers import CollectionSerializer, MovieSerializer, GenreCountSerializer

from rest_framework.test import APITestCase

class CollectionserilizerTestcase(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='test_username',password = "test_password", email = 'test_mail@test.com')
        self.collection = Collection.objects.create(title = "test_title",
                                                    description = "test_description",
                                                    user = self.test_user)
    def test_collection_serializer(self):
        
        _data = {
            'title' : 'test_title',
            'description' : 'test_description',
            'user': 1
        }
        
        collection = CollectionSerializer(data = _data) 
        
        self.assertTrue(collection.is_valid()) 
        
    def test_movie_serializer(self):
         
        _data = {
            'title': 'movie_title',
            'description': 'movie_description',
            'genres': "A,B,C" ,
            'uuid' : '0300ce42-7327-4d57-8466-d3ce650b458b'
        }
        
        movie = MovieSerializer(data = _data)
        
        self.assertTrue(movie.is_valid())