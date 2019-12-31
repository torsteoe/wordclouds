from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np
import requests
from bs4 import BeautifulSoup
currdir = os.path.dirname(__file__)

def get_page_text(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    text = soup.body.find('div', {"class": ["postcell post-layout--right"]})
    return text.text
def create_wordcloud(text, outFile):
    mask = np.array(Image.open(os.path.join(currdir, "cloud.png")))
    stopwords = set(STOPWORDS)
    wc = WordCloud(stopwords=stopwords, mask=mask, background_color="white", max_words=200)
    wc.generate(text)
    wc.to_file(os.path.join(currdir, outFile))
#print(get_page_text("https://stackoverflow.com/questions/4181861/message-src-refspec-master-does-not-match-any-when-pushing-commits-in-git"))
create_wordcloud(get_page_text("https://stackoverflow.com/questions/4181861/message-src-refspec-master-does-not-match-any-when-pushing-commits-in-git"), "stack.png")
