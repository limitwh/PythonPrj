__author__ = 'limitwh'
#coding=utf-8
import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()
XML={}
#print(database.attrib['name'])
#print(password)
for child in root:
	XML['dbname']=child.attrib['name']
	for x in child:
		XML[x.tag]=x.text
print(XML)