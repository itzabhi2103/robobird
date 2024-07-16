from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup= BeautifulSoup(yc_web_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_title = [movie.getText() for movie in all_movies]

movies = movie_title[::-1]

with open("movies.txt", mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")