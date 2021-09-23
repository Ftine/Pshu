# coding: utf-8
# @TIME:2021/8/1 20:11
# @Author: ckj

from bs4 import BeautifulSoup
import re

'''
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,
所有对象可以归纳为4种: 
Tag（第一个查找标签中（<a></a>）的内容）,
NavigableString (标签里面的内容)
BeautifulSoup (表示整个文档)
Comment 
'''

file = open("login.html", 'rb')
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")
# print(bs.title)
# print(bs.header.a.attrs) #(标签里面的内容 属性值 形成字典<a href="index.html" target="_blank">)
# print(bs.h1.string)

# ————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————
# 文档的遍历
# print(bs.head.contents[3])

# 文档的搜索：find_all
# find_all 获取所有的某标签形成列表返回，
# a_list = bs.find_all('a')
# 利用正则表达式搜索
# a_list = bs.find_all(re.compile('a'))  # 返回标签带a的所有标签
# 利用函数搜索
# def name_is_exist(tag):
#     return tag.has_attr("name")
# a_list=bs.find_all(name_is_exist)  # 搜索标签内有name属性的标签
# print(a_list)


# kwarg 参数
# find_all( name , attrs , recursive , string , **kwargs )
# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件.
# t_list=bs.find_all(type="text")
# t_list=bs.find_all(class_=True) #返回到class的属性的标签
# t_list = bs.find_all(text=['微信', 'QQ'])
# text=re.compile('\d') #找数字

# for i in t_list:
#     print(i)

# css选择器 列表返回
# print(bs.select('title'))  # 按标签
# print(bs.select('.clear_btn'))  # 使用类名查找 class="clear_btn"
# print(bs.select('#pwd'))  # 通过id="xxx"查找
# print(bs.select('div[class="item item-border"]'))  # 通过标签加属性查找<div class="item item-border">
# print(bs.select('header > a'))   # <header> <a href

t_list=bs.select(".item item2 ~ .item")
print(t_list)