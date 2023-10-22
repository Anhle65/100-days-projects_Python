import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
responses = response.text
# print(responses)
data = BeautifulSoup(responses, "html.parser")
lists = []
titles = data.find_all(name='h3', class_="listicleItem_listicle-item__title__hW_Kn")
for each in titles:
    lists.insert(0, each.getText())
for i in lists:
    print(i)
with open('movie.txt', mode='w') as file:
    for i in lists:
        file.write(f'{i}\n')


