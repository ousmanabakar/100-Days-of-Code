from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_website = response.text
soup = BeautifulSoup(yc_website, "html.parser")


articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()  # article_tag.string
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_up_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_vote = max(article_up_votes)
max_vote_article = article_up_votes.index(max_vote)

print(article_texts[max_vote_article])
print(article_links[max_vote_article])

# print(article_texts)
# print(article_links)
# print(article_up_votes)




