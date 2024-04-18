# from django.urls import HttpResponse
from django.http import HttpResponse , JsonResponse
def home_page(requst):
    print("home page requested")
    friends=[
        'junaid',
        'gazi',
        'ankit',
        'nikhil'
    ]
    return JsonResponse(friends, safe=False)