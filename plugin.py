# Example plugin for Lampa with movie sources from uakino.me and rezka-ua.org

import requests
from bs4 import BeautifulSoup

# Function to fetch data from the websites
def get_movies():
    movies = []

    # Fetching movies from uakino.me
    uakino_url = "https://uakino.me"
    uakino_response = requests.get(uakino_url)
    if uakino_response.status_code == 200:
        uakino_soup = BeautifulSoup(uakino_response.text, 'html.parser')
        for movie in uakino_soup.find_all('a', class_='movie-link'):
            title = movie.get('title')
            link = movie.get('href')
            movies.append({'title': title, 'link': link})

    # Fetching movies from rezka-ua.org
    rezka_url = "https://rezka-ua.org"
    rezka_response = requests.get(rezka_url)
    if rezka_response.status_code == 200:
        rezka_soup = BeautifulSoup(rezka_response.text, 'html.parser')
        for movie in rezka_soup.find_all('a', class_='b-content__inline_item-link'):
            title = movie.get('title')
            link = movie.get('href')
            movies.append({'title': title, 'link': link})

    return movies

# Function to display the movies
def display_movies():
    movies = get_movies()
    for movie in movies:
        print(f"Title: {movie['title']}, Link: {movie['link']}")

# Call the function to display the movies
if __name__ == "__main__":
    display_movies()

