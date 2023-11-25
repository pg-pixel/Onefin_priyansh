from django.db import models


from users_app.models import User
import uuid
# Create your models here.

    
class Collection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genres = models.CharField(max_length = 1000, default='' )
    uuid = models.UUIDField()
    collection = models.ManyToManyField(Collection)
    
class GenreCount(models.Model):
    user_id = models.IntegerField(default = 1)
    genre_name = models.CharField(max_length=100)
    genre_count = models.IntegerField(default = 1)