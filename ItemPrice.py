__author__ = 'limitwh'
#coding=utf-8
import requests
import json

def GetPrice(str):
	PriceUrl = "https://p.3.cn/prices/mgets?skuIds=J_"+str
	Price=requests.get(PriceUrl).json()
	return Price[0]['op']

print(GetPrice("5544080"))