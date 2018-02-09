__author__ = 'limitwh'
#coding=utf-8
import requests
import json
Itemres=requests.get("https://p.3.cn/prices/mgets?skuIds=J_5544080").json()
print(Itemres[0]['op'])