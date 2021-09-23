# coding: utf-8
# @TIME:2021/8/3 19:59
# @Author: ckj

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("新的表格页面")
worksheet.write(0,0,'holle')
workbook.save('新的.xls')