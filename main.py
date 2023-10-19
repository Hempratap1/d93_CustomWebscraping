import csv
from bs4 import BeautifulSoup
import requests

URL = "https://www.imdb.com/search/title/?at=0&genres=animation&keywords=anime&num_votes=1000,&sort=user_rating&title_type=tv_series"

response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")

anime_rating = soup.select("div .lister div div strong")
anime_title = soup.select("div .lister h3 a")

animes = [anime.get_text() for anime in anime_title]
ratings = [rating.get_text() for rating in anime_rating]

anime_dict = {anime: rating for anime, rating in zip(animes, ratings)}
print(anime_dict)
csv_file_path = 'anime_ratings.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Anime', 'Rating'])
    for anime, rating in anime_dict.items():
        writer.writerow([anime, rating])

print(f'CSV file "{csv_file_path}" has been created.')