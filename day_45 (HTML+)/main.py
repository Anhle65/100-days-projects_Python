from bs4 import BeautifulSoup
import requests
data = requests.get("https://news.ycombinator.com/")
beauty = BeautifulSoup(data.text, "html.parser")
titles_list = []
scores_list = []
links_list = []
# titles = beauty.find_all(name='span', class_='titleline')
titles = beauty.select(selector='.titleline a')
for each in titles:
    titles_list.append(each.getText())
title_links = beauty.find_all(name='span', class_='titleline')
for link in title_links:
    links_list.append(link.find(name='a').get('href'))
score = beauty.select(selector=".score")
for a in score:
    scores_list.append(int(a.getText().split(' ')[0]))
    indexs = scores_list.index(max(scores_list))
print(links_list[indexs])
print(scores_list[indexs])
print(titles_list[indexs])
print(links_list)
print(scores_list)
print(titles_list)













# import lxml

# with open("website.html", encoding="utf8") as file:
#     content = file.read()
#     # print(content)
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title.name)
# print(soup.find_all('p'))
# print(soup.title.string)
# for link in soup.find_all("a"):
#     print(link.get("href"))


