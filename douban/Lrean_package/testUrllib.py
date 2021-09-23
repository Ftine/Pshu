# coding: utf-8
# @TIME:2021/8/1 11:41
# @Author: ckj

import urllib.request
import urllib.parse  # 数据解析器

# get方式获取网址
# response = urllib.request.urlopen("http://baidu.com")
# print(response.read().decode('utf-8'))
#超时问题
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e :
#     print("error:time out")


# post方式访问 需要传递参数 利用parse封装
# data=bytes(urllib.parse.urlencode({"name":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode())


# response = urllib.request.urlopen("http://baidu.com")
# response.status
# print(response.getheader("Server"))

#伪装浏览器访问
# url="http://httpbin.org/post"
# headers={
#     "User-Agent":
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
# }
# data=bytes(urllib.parse.urlencode({"name":"world"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url="http://douban.com"
headers={
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
