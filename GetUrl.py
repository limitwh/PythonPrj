__author__ = 'limitwh'
#coding=utf-8
import requests
import re
def GetItemFromUrl(url):
	Urlres=requests.get(url)
	Regres=re.compile(r"item.jd.com.*?html")
	PriceID=re.compile(r"\d+")
	TempUrlLists=Regres.findall(str(Urlres.content,'utf-8'))
	PriceIDList=PriceID.findall(''.join(TempUrlLists))
	TempList=[]
	for x in TempUrlLists:
		TempList.append("https://"+x)
	TempDic=dict(zip(PriceIDList,TempList))
	return TempDic

UrlDict = GetItemFromUrl("https://list.jd.com/list.html?cat=9987,653,655")
for key in UrlDict:
	print(key+':'+UrlDict[key]) 