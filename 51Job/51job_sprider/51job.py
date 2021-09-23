# coding: utf-8
# @TIME:2021/8/7 10:47
# @Author: ckj

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式进行文字匹配
import urllib.error, urllib.request  # 指定url，获取网页数据
import mysql.connector
import json


def mainFunction():
    for i in range(2, 11):  # 爬取十个页面的信息
        num = str(i)
        baseurl = "https://search.51job.com/list/040000,000000,0000,00,9,99,java,2," + num + ".html"  # python
        basehtml = getWebByUrl(baseurl)  # 获取web页面Html
        # print(basehtml)
        dataList = getDataByHtml(basehtml)


def getWebByUrl(baseurl):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }  # 用户代理，伪装成浏览器访问
    req = urllib.request.Request(url=baseurl, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("gbk")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getDataByHtml(html):
    # 对网页进行逐一解析
    soup = BeautifulSoup(html, "html.parser")
    ans = soup.select("body > script")
    result = ans[1].string
    text = " "
    text = result + text
    info = text[29:]
    # print(info)
    job_info = json.loads(info)
    job_list_info = job_info['engine_search_result']

    # print(job_list_info)
    init_DataDb()
    con = mysql.connector.connect(
        host='localhost', port=3306,
        user='root', password='root',
        database='51job'
    )
    cursor = con.cursor()
    for item in job_list_info:
        dataString = []
        job_name = '"' + item['job_name'] + '"'
        dataString.append(job_name)

        job_href = '"' + item['job_href'] + '"'
        dataString.append(job_href)

        company_name = '"' + item['company_name'] + '"'
        dataString.append(company_name)

        workarea_text = '"' + item['workarea_text'] + '"'
        dataString.append(workarea_text)

        providesalary_text = '"' + item['providesalary_text'] + '"'
        dataString.append(providesalary_text)

        if len(item['attribute_text']) < 4:
            attribute_text = " "
        else:
            attribute_text = '"' + item['attribute_text'][2] + '"'
        dataString.append(attribute_text)

        companyind_text = '"' + item['companyind_text'] + '"'
        dataString.append(companyind_text)

        jobwelf = '"' + item['jobwelf'] + '"'
        dataString.append(jobwelf)
        sql = '''
         insert into 51job (job_name,job_href,company_name,workarea,providesalary,education,profession,jobwelf)
         value (%s)''' % ",".join(dataString)
        try:
            cursor.execute(sql)
            con.commit()
        except mysql.connector.errors.ProgrammingError:
            continue
    cursor.close()
    con.close()


def init_DataDb():
    con = mysql.connector.connect(
        host='localhost', port=3306,
        user='root', password='root',
        database='51job'
    )
    cursor = con.cursor()
    sql = '''
    create table if not exists 51job (
    id integer primary key auto_increment,
    job_name text,
    job_href text,
    company_name text,
    workarea text,
    providesalary text ,
    education varchar(10),
    profession  text,
    jobwelf text)
    '''
    cursor.execute(sql)
    cursor.close()
    con.close()
    return


if __name__ == "__main__":
    mainFunction()
