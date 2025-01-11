import requests
import random
import os

class GenreNotFound(Exception):
    pass

class MovieNotFound(Exception):
    pass

try:

    API_KEY = os.environ.get("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={API_KEY}"
    headers = {"accept": "application/json"}

    genres = requests.get(url, headers=headers).json()

    print("Available genres:")

    genre_id = dict()

    for genre in genres["genres"]:
        genre_id[genre["name"]] = genre["id"]
        print(f"- {genre["name"]}")

    genre = input("Enter a genre from list above: ").strip()

    if genre not in genre_id.keys():
        raise GenreNotFound
    
    url = f"https://api.themoviedb.org/3/discover/movie?with_genres={genre_id[genre]}&language=en&sort_by=popularity.desc&page=1&api_key={API_KEY}"

    movies = requests.get(url,headers=headers).json()["results"]
    if len(movies)==0:
        raise MovieNotFound

    random_movie = random.choice(movies)
    print("\n🎬 Recommended Movie:")
    print(f"Title: {random_movie.get('title', 'Unknown')}")
    print(f"Overview: {random_movie.get('overview', 'No description available.')}")
    print(f"Release Date: {random_movie.get('release_date', 'Unknown')}")
    print(f"Rating: {random_movie.get('vote_average', 'N/A')}")

except GenreNotFound as e:
    print("Given genre is not listed.")
except MovieNotFound as e:
    print("No movies found for the given genre.")
except ConnectionError as e:
    print("Connection error.")
except Exception:
    print("Error occured.")