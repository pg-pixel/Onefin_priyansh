from django.test import TestCase 

from movies_app.models import Collection, Movie, GenreCount 
from users_app.models import User 

class CollectionmodelTest(TestCase):
    
    def setUp(self):
        self.test_user = User.objects.create(username='test_username',password = "test_password", email = 'test_mail@test.com')
        self.collection = Collection.objects.create(title = "test_title",
                                                    description = "test_description",
                                                    user = self.test_user)
        
    def test_create_collection(self):
        test_user = self.test_user
        title = "test_title"
        description = "test_description" 
        user = test_user 
        
        collection = Collection.objects.create(title = title, description = description , user = test_user) 
        
        self.assertEqual(collection.title, title)
        self.assertEqual(collection.description, description)
        self.assertEqual(collection.user, test_user) 
        
    def test_create_movie(self):
        title = 'movie_title'
        description = 'movie_description'
        genres = "genre_A, genre_B, genre_C"
        uuid = "0300ce42-7327-4d57-8466-d3ce650b458b"
        collection = self.collection 
        
        movie = Movie.objects.create(title = title, description = description, genres = genres,
                                     uuid = uuid) 
        
        movie.collection.add(collection)
        
        self.assertEqual(movie.title, title)
        self.assertEqual(movie.description, description) 
        
    def test_create_genre_count(self):
        user_id = 1
        genre_name = "test_genre_name"
        expected_genre_count = 1 
        
        genre_count = GenreCount.objects.create(user_id = user_id, genre_name = genre_name, 
                                                genre_count = expected_genre_count) 
        
        self.assertEqual(genre_count.genre_count, expected_genre_count)
        self.assertEqual(genre_count.user_id, user_id)
        self.assertEqual(genre_count.genre_name, genre_name)
        
        
        
        