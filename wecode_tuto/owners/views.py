import json
from django.http import JsonResponse, HttpResponse
from owners.models import *
from django.views import View

# Create your views here.
class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owners.objects.create(name=data['name'],age=data['age'],email=data['email'])
        return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)
    
    def get(self, request):
        owners = Owners.objects.all()
        dogs = Dogs.objects.all()
        owners_results = []
        dog_list = []
        for owner in owners:
            for dog in dogs:
                if owner.id == dog.owners_id:
                    dog_list.append({'dog_name':dog.name,'dog_age':dog.age})
                owners_results.append(
                    {
                        "name":owner.name,
                        "email":owner.email,
                        "age":owner.age,
                        "dog_list":dog_list,
                    }
                )
        return JsonResponse({'owners_results':owners_results}, status = 200)

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        owners = Owners.objects.all()
        for owner in owners:
            if owner.name == data['owner']:
                Dogs.objects.create(name=data['name'],age=data['age'],owners=owner)
                return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)
            else:
                return JsonResponse({'MESSAGE':'FAIL'}, status = 404)
        
    def get(self, request):
        dogs = Dogs.objects.all()
        dogs_results = []
        for dog in dogs:
            dogs_results.append(
                {
                    "name":dog.name,
                    "age":dog.age,
                }
            )
        return JsonResponse({'dogs_results':dogs_results}, status = 200)