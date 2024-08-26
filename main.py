from bs4 import BeautifulSoup
import requests
import lxml


connection = requests.get("https://news.ycombinator.com/")
text_connection = connection.text

soup = BeautifulSoup(text_connection, "html.parser")
title = soup.title
article_name = soup.find("span", class_="titleline")
new = article_name.find(name="a").getText()
news = article_name.get("a")
# article_name_text = article_name.getText()
# article_link = article_name.find("href", class_="titleline")
article_score = soup.find("span", class_="score").getText()
print(article_name)
print(new)
print(news)
print(article_score)
# print(article_score.getText())
# print(article_link)



# with open("website.html") as myweb:
#     contents = myweb.read()
#     # print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
#
# allsss = soup.find_all(name="a")
# print(allsss)
#
# heading = soup.find(name="h1", id="name")
#