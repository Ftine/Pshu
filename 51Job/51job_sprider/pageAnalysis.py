# coding: utf-8
# @TIME:2021/8/7 20:09
# @Author: ckj

from bs4 import BeautifulSoup
import  json
html = open("jobWeb.html",'r')
soup = BeautifulSoup(html, "html.parser")

# result = soup.select()
ans = soup.select("body > script")
result = ans[1].string
text = " "
text = result + text
info = text[32:]
uesr_info = json.loads(info)
job_list_info = uesr_info['engine_search_result']
#print(job_list_info)

for item in job_list_info:
    dataString = []
    job_name = '"'+item['job_name']+'"'
    dataString.append(job_name)

    job_href = '"'+item['job_href']+'"'
    dataString.append(job_href)

    company_name = '"'+item['company_name']+'"'
    dataString.append(company_name)

    workarea_text = '"'+item['workarea_text']+'"'
    dataString.append(workarea_text)

    providesalary_text = '"'+item['providesalary_text']+'"'
    dataString.append(providesalary_text)

    if len(item['attribute_text']) < 4:
        attribute_text = " "
    else:
        attribute_text = '"' + item['attribute_text'][2] + '"'
    dataString.append(attribute_text)

    companyind_text = '"'+item['companyind_text']+'"'
    dataString.append(companyind_text)

    jobwelf = '"'+item['jobwelf']+'"'
    dataString.append(jobwelf)
    print(dataString)

# 'job_name'
# 'job_href'
# 'company_name'
# 'workarea_text' 工作地点
# 'providesalary_text' 工资
# 'attribute_text' 学历要求       item['attribute_text'][2]
# 'companyind_text' 工作行业
# 'jobwelf' 工作福利


