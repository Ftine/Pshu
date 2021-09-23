# coding: utf-8
# @TIME:2021/8/1 10:59
# @Author: ckj

import xlwt  # Ecexl
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式进行文字匹配
import urllib.error, urllib.request  # 指定url，获取网页数据
import sqlite3
import mysql.connector

'''
1.爬取网页
2.解析数据
3.分析数据
'''


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取数据
    datalist = getData(baseurl)

    # savePath = r"./豆瓣数据.xls"
    # 保存数据
    # saveData(datalist,savePath)
    sava2DataDB(datalist)
    # askUrl(baseurl)


findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式规范，寻找电影链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S使包含换行符 获取图片的链接
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页，逐一解析数据
def getData(baseurl):
    datalist = []
    for i in range(10):  # 获取页面信息十次
        url = baseurl + str(i * 25)
        html = askUrl(url)  # 保存获取网页源码

        # 对网页进行逐一解析
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 从html页面寻找先获取的信息内容所属标签("span", class_="title")  形成列表
            # print(item)
            item = str(item)
            data = []  # 保存一部电影的所有信息
            link = re.findall(findLink, item)[0]  # 返回字列表
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            title = re.findall(findTitle, item)
            if len(title) == 2:
                ctitle = title[0]
                data.append(ctitle)
                ftitle = title[1].replace("/", "")
                data.append(ftitle)
            else:
                data.append(title[0])
                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judge = re.findall(findJudge, item)[0]
            data.append(judge)

            inp = re.findall(findInq, item)
            if len(inp) != 0:
                inp = inp[0].replace("。", " ")
                data.append(inp)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub(r'<br(\s+)?/>(\s+)?', ' ', bd)
            bd = re.sub('/', ' ', bd)
            data.append(bd.strip())  # 一个电影数据成一个数据列表

            datalist.append(data)
    # print(datalist)

    return datalist


def askUrl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
    }  # 用户代理，伪装成浏览器访问
    req = urllib.request.Request(url=url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("豆瓣电影TOP250", cell_overwrite_ok=True)
    col = ('电影详情链接', '图片链接', '电影中文名称', '外文名称', '评分', '评价人数', '简介', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 存标题
    for i in range(0, 250):
        print(f'第{i}条')
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])  # 存数据
    book.save("豆瓣数据爬取.xls")

    return


def sava2DataDB(datalist):
    init_DataDb()
    con = mysql.connector.connect(
        host='localhost', port=3306,
        user='root', password='root',
        database='douban'
    )
    cursor = con.cursor()
    for data in datalist:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        # sql = '''
        #     insert into movie250 (info_link,pic_link,cname,fname,score,rated,in_te,info_movie)
        #      values(%s)''' % ",".join(data)
        # # print(sql)
        # # break
        print(data)
        # cursor.execute()
        # con.commit()
    cursor.close()
    con.close()

def init_DataDb():
    con = mysql.connector.connect(
        host='localhost', port=3306,
        user='root', password='root',
        database='douban'
    )
    cursor = con.cursor()
    sql = '''
    create table if not exists movie250 (
    id integer primary key auto_increment,
    info_link text,
    pic_link text,
    cname varchar(100),
    fname varchar(100),
    score float ,
    rated numeric,
    in_te text,
    info_movie text) 
    '''
    cursor.execute(sql)
    cursor.close()
    con.close()
    return


if __name__ == "__main__":
    main()
