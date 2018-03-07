__author__ = 'limitwh'
#coding=utf-8
import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()
for child in root:
	print(child.tag,child.attrib)
	for x in child:
		print(x.tag,x.text)