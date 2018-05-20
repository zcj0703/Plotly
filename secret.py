# coding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import  jieba
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

url1 = 'https://movie.douban.com/subject/2124724/comments?start='
url2 = '&limit=20&sort=new_score&status=P&percent_type='

comment_list = []

def each_page(n):
    wb_data = requests.get(url1 + str(n) + url2)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    comment_div_list = soup.select('div.comment > p')

    for item in comment_div_list:
        #print(item.text.strip())

        comment_list.append(item.text.strip())



for i in range(2100):
    #print(i)
    each_page(i*20)

comments = ''
for k in range(len(comment_list)):
    comments = comments + (str(comment_list[k])).strip()
pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comments = ''.join(filterdata)

jieba.add_word('桂纶镁')
cut_text = jieba.cut(cleaned_comments)
result = '/'.join(cut_text)

stopwords = set(STOPWORDS)
st = open('stopword.txt', 'rb')
for line in st:
    stopwords.add(line)


image = Image.open('love.jpg')
img = np.array(image)
wc = WordCloud(font_path="simhei.ttf", background_color='white', max_font_size=70, mask=img)
wc.generate(str(result))

image_color = ImageColorGenerator(img)
wc.recolor(color_func=image_color)
wc.to_file(r"wordcloud.png")

plt.imshow(wc)
plt.axis("off")
plt.show()