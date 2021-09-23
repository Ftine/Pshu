# coding: utf-8
# @TIME:2021/8/3 10:32
# @Author: ckj

import re

pat = re.compile("AA")  # 寻找包含AA的字符串
# ans = pat.search("ABCCAA")   # 进行匹配搜索
# ans = re.search('Asd','bkbdsjASdAsd') #前者是规则（正则表达式）
# ans = re.findall('[A-Z]+','skjsbASDfHHHkAsAZZdbfasd')
ans = re.sub('a','A','aHHHasbahjdvsjfJJJ')
print(ans)
