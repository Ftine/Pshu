# coding: utf-8
# @TIME:2021/8/6 17:58
# @Author: ckj

import jieba  # 分词
import matplotlib.pyplot as plt
from matplotlib import pyplot  # 绘图，数据可视化
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np
import mysql.connector

con = mysql.connector.connect(
    host='localhost', port=3306,
    user='root', password='root',
    database='douban'
)
cursor = con.cursor()
sql = '''
    select in_te from movie250
    '''
data = cursor.execute(sql)
datalist = cursor.fetchall()
#print(datalist)  元组列表[('希望让人自由 ',), ('风华绝代 ',)]
text = ""
for item in datalist:
    text = text + item[0]
#print(text)
cursor.close()
con.close()

#字符串分词
wordString = jieba.cut(text)
words_string = ' '.join(wordString)
print(len(words_string))

img = Image.open(r'./static/assets/img/tree.jpg')
img_array = np.array(img)  # 将图片转化为数组
wc = WordCloud(
    background_color="white",
    mask=img_array,
    font_path="msyh.ttc",
)
wc.generate_from_text(words_string)   # 利用分好的图 准备绘制图片的对象

# 绘制图片 利用词语
fig = plt.figure(1)
plt.imshow(wc)
plt.axis("off")
#plt.show()

plt.savefig(r'./static/assets/img/wordtree.jpg',dpi=500)
