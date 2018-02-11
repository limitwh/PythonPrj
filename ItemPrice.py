__author__ = 'limitwh'
#coding=utf-8
import requests
import json
#Itemres=requests.get("https://p.3.cn/prices/mgets?skuIds=J_5544080").json()
#print(Itemres[0]['op'])

def GetPrice(str):
	PriceUrl = "https://p.3.cn/prices/mgets?skuIds=J_"+str
	Price=requests.get(PriceUrl).json()
	return Price[0]['op']

print(GetPrice("5544080"))