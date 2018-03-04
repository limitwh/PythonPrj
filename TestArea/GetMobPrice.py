__author__ = 'limitwh'
#coding=utf-8
from bs4 import BeautifulSoup
import requests
import re
MobPriceUrl="https://list.jd.com/list.html?cat=9987,653,655&page=1"
Regres=re.compile(r"item.jd.com.*?html")
PriceID=re.compile(r"\d+")
htmlstr=requests.get(MobPriceUrl).text
soup = BeautifulSoup(htmlstr,"lxml")
tagstr = str(soup.find_all(name='ul',attrs={"class":"gl-warp clearfix"})[0])
TempUrlLists=Regres.findall(tagstr)
PriceIDList=PriceID.findall(''.join(TempUrlLists))
print(TempUrlLists)
print(PriceIDList)