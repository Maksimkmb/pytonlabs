from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from collections import Counter
import matplotlib.pyplot as plt


websites = ['https://www.radiosvoboda.org/news']


driver = webdriver.Chrome()  



def get_news_texts(url, year, month):
    archive_url = f"{url}/archive/{year}/{month}"
    driver.get(archive_url)
    time.sleep(2)  

    news_texts = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        text = article.get_text(strip=True)
        news_texts.append(text)

    return news_texts



all_words_counter = Counter()

for website in websites:
    for year in range(2022, 2023):  
        for month in range(1, 13):
            news_texts = get_news_texts(website, year, month)
            

            all_text = ' '.join(news_texts)
            words = all_text.lower().split()
            word_counter = Counter(words)
            all_words_counter += word_counter


common_words = all_words_counter.most_common(10)  


for word, count in common_words:
    print(f'{word}: {count}')

labels, values = zip(*common_words)
indexes = range(len(labels))

plt.bar(indexes, values, align='center')
plt.xticks(indexes, labels)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Most Common Words in News')
plt.show()


driver.quit()
