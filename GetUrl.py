__author__ = 'limitwh'
#coding=utf-8
import requests
import re
Urlres=requests.get("https://list.jd.com/list.html?cat=9987,653,655")
Regres=re.compile(r"item.jd.com.*?html")
PriceID=re.compile(r"\d+")
TempUrlLists=Regres.findall(str(Urlres.content,'utf-8'))
PriceIDList=PriceID.findall(''.join(TempUrlLists))
UrlLists=[]
for x in TempUrlLists:
	UrlLists.append("https://"+x)
ItemDic=dict(zip(PriceIDList,UrlLists))
print(ItemDic)