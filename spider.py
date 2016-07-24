import requests
import re
from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')
namelist = bs.find_all('span',{'class','green'})      #获取网页上所有的绿色字符
test = bs.find_all(text='the prince')
print(len(test))
print('=============================================================================================================')
#get_text()用来把正在处理的html文档中的所有标签清除，然后返回一个只包含文字的字符串
for i in namelist:
    print(i.get_text())

