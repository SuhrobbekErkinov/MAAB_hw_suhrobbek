import requests
import random


def get_genre_id(genre_name, api_key):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    response = requests.get(url)

    if response.status_code == 200:
        genres = response.json().get("genres", [])
        for genre in genres:
            if genre["name"].lower() == genre_name.lower():
                return genre["id"]
        print("Genre not found.")
    else:
        print("Error fetching genres.")
    return None


def get_random_movie(genre_id, api_key):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    response = requests.get(url)

    if response.status_code == 200:
        movies = response.json().get("results", [])
        if movies:
            return random.choice(movies)
        else:
            print("No movies found for this genre.")
    else:
        print("Error fetching movies.")
    return None


def main():
    api_key = "YOUR_API_KEY"  # Replace with your TMDB API key
    genre_name = input("Enter a movie genre: ")
    genre_id = get_genre_id(genre_name, api_key)

    if genre_id:
        movie = get_random_movie(genre_id, api_key)
        if movie:
            print(f"Recommended Movie: {movie['title']}\nOverview: {movie['overview']}")


if __name__ == "__main__":
    main()
