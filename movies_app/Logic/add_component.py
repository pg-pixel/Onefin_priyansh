from movies_app.models import Collection, Movie, GenreCount
from users_app.models import User
from movies_app.serializers import CollectionSerializer, MovieSerializer, GenreCountSerializer

class Add_component:
    @staticmethod 
    def add_new_collection(user, request_data, collection_data):
        try:
            collection_serializer = CollectionSerializer(data = collection_data)
            if collection_serializer.is_valid():
                collection = collection_serializer.save() 
                _set = set()
                # add movies 
                Add_component.add_movie(request_data.get("movies", []), collection, user, _set)
        except Exception as exp:
            if collection:
                collection.delete()
            data = {
                "message": f"Error while adding collection. Exception is: {exp}",
            }
            
            status = 500
            return data, status
        else:
            data = {
            "collection id": collection.id,
            }
            
            status = 200
            return data, status
    
    @staticmethod
    def update_collection(user, request_data, collection_data, collection):
        try:
            serializer = CollectionSerializer(collection, data=collection_data, partial = True)
            if serializer.is_valid():
                serializer.save()
                collection.refresh_from_db() 
                
                # get movies based on collection id
                _set = set() 
                movies = Movie.objects.filter(collection = collection) 
                for movie_info in MovieSerializer(movies, many=True).data:
                    _set.add(movie_info['uuid'])
                
                # add movies
                Add_component.add_movie(request_data.get("movies", []), collection, user, _set)
        except Exception as Exp:
            data = {
                'message': "collection updation failed. Exception is : {Exp}"
            }
            status = 500
            return data, status 
        else:
            movies = Movie.objects.filter(collection = collection)  
            data = {
            "title" : collection.title,
            "description" : collection.description,
            "movies" : MovieSerializer(movies, many=True).data
            }   
            status = 200 
            return data, status
        
    @staticmethod
    def add_movie(movie_lst, collection, user, _set):
        try:
            for movie_data in movie_lst:
                if movie_data["uuid"] not in _set:
                    movie_serializer = MovieSerializer(data = movie_data)
                    if movie_serializer.is_valid():
                        movie = movie_serializer.save()
                        movie.uuid = movie_data["uuid"]
                        movie.collection.add(collection)
                        movie.save()
                        # update genre count
                        Add_component.update_genre_count(movie, user)
        except Exception as exp:
            if movie:
                movie.delete()
            raise Exception(f" Error while adding movie. Exception is : {exp}")
                                
    @staticmethod 
    def update_genre_count(movie, user):
        try:
            for genre in movie.genres.split(','):
                genre_count = GenreCount.objects.filter(user_id = user.id, genre_name = genre).first()
                if genre_count:
                    genre_count.genre_count += 1 
                    genre_count.save()
                else:
                    genre_data = {
                        "user_id": user.id, 
                        "genre_name": genre
                    } 
                    genre_serializer = GenreCountSerializer(data = genre_data) 
                    if genre_serializer.is_valid():
                        genrecount = genre_serializer.save()
        except Exception as Exp:
            raise Exception(f"Error while updating genre count. Exception: {Exp}")