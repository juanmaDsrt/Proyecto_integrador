from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
import matplotlib.pyplot as plt
import io
import urllib, base64
import matplotlib
matplotlib.use('Agg')

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

def statistics_view(request):
    all_movies = Movie.objects.all()

    # 📊 **Películas por año**
    movie_counts_by_year = {}
    for movie in all_movies:
        year = str(movie.year) if movie.year else "Unknown"  # Convertir a str
        movie_counts_by_year[year] = movie_counts_by_year.get(year, 0) + 1

    # 📊 **Películas por género**
    movie_counts_by_genre = {}
    for movie in all_movies:
        if movie.genre:  # Verificar si tiene género
            genres = movie.genre.split(',')
            for genre in genres:
                genre = genre.strip()
                if genre:  # Evitar valores vacíos
                    movie_counts_by_genre[genre] = movie_counts_by_genre.get(genre, 0) + 1

    # 🔹 **Generar gráfico de películas por año**
    buffer_year = io.BytesIO()
    plt.figure(figsize=(8,5))
    plt.bar(list(movie_counts_by_year.keys()), list(movie_counts_by_year.values()), color='blue')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.title('Movies per Year')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(buffer_year, format='png')
    buffer_year.seek(0)
    graphic_year = base64.b64encode(buffer_year.getvalue()).decode('utf-8')
    plt.close()

    # 🔹 **Generar gráfico de películas por género**
    buffer_genre = io.BytesIO()
    plt.figure(figsize=(8,5))
    plt.bar(list(movie_counts_by_genre.keys()), list(movie_counts_by_genre.values()), color='green')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.title('Movies per Genre')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(buffer_genre, format='png')
    buffer_genre.seek(0)
    graphic_genre = base64.b64encode(buffer_genre.getvalue()).decode('utf-8')
    plt.close()

    return render(request, 'statistics.html', {
        'graphic_year': graphic_year,
        'graphic_genre': graphic_genre
    })

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})