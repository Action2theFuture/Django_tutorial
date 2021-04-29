import json
from django.http import JsonResponse, HttpResponse
from movies.models import *
from django.views import View

# Create your views here.
class ActorsView(View):
    def post(self, request):
        data = json.loads(request.body)
        actor = Actors.objects.create(
            first_name=data['first_name'], 
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth'],
            )
        movies = Movies.objects.all()
        for movie in movies:
            if movie.title == data['movie']:
                actor.movies.add(movie.id)
        return JsonResponse({'MASSAGE':'SUCCESS'}, status = 201)
    def get(self,request):
        actors = Actors.objects.all()
        movies = Movies.objects.all()
        results = []
        for actor in actors:
            results.append(
                {
                    'first_name':actor.first_name,
                    'last_name':actor.last_name,
                    'birth':actor.date_of_birth,
                    'title':[i.title for i in actor.movies.all()]
                }
            )
            print(actor.movies.filter(id=actor.id))
        return JsonResponse({'actors_results':results}, status = 200)

class MoviesView(View):
    def post(self, request):
        data = json.loads(request.body)
        movie = Movies.objects.create(
            title=data['title'],
            release_date=data['release_date'],
            running_time=data['running_time'],
        )
        actors = Actors.objects.all()
        for actor in actors:
            if actor.first_name == data['first_name']:
                movie.actors.add(actor.id)
        return JsonResponse({'MASSAGE':'SUCCESS'}, status = 201)
    def get(self, request):
        movies = Movies.objects.all()
        result = []
        for movie in movies:
            result.append({
                'title':movie.title,
                'running_time':movie.running_time,
                'actor':[i.first_name for i in movie.actors.all()]
            })
        return JsonResponse({'movie_result':result}, status = 200)