__author__ = 'limitwh'
#coding=utf-8
import re
pricelist=[['10471380245', '699.00'], ['1057746', '暂无报价'], ['10695001327', '暂无报价']]
PriceID=re.compile(r"^\d+?\.\d+?$")
for price in pricelist:
	if (len(PriceID.findall(price[1])) == 0):
		price[1]='-1'
print(pricelist)