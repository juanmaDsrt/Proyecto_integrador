from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.


def home(request):
    "return HttpResponse('<h1>Welcome to Home Page</h1>')"
    "return render(request,'home.html',{'name': 'Juan Manuel Florez'})"
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})


from django.shortcuts import render
def about(request):
    return render(request, 'about.html')
