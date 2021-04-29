from django.db import models

# Create your models here.
class Actors(models.Model):
    id = models.BigAutoField(primary_key = True)
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length= 45)
    date_of_birth = models.DateField()
    movies = models.ManyToManyField('Movies', through ="Actors_Movies", verbose_name="movies", related_name='actors')
    
    def __str__(self):
        return self.last_name

    class Meta:
        db_table = "actors"

class Movies(models.Model):
    id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length = 45)
    release_date = models.DateField(null=True, blank=True)
    running_time = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "movies"

class Actors_Movies(models.Model):
    id = models.BigAutoField(primary_key=True)
    actor = models.ForeignKey("Actors", on_delete=models.CASCADE, verbose_name = "actors")
    movie = models.ForeignKey("Movies", on_delete=models.CASCADE, verbose_name = "movies")

    class Meta:
        db_table = "actors_movies"