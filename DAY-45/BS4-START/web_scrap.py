from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome('chromedriver')
url = 'https://www.empireonline.com/movies/features/best-movies-2/'
browser.get(url)
html_source = browser.page_source

f = open('movies.txt', 'w', encoding='utf-8')
f.writelines(html_source)
f.close()

with open("movies.txt") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
article_films = [score.getText() for score in soup.find_all(name="h3")]
movies = article_films[::-1]
with open("watch.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")