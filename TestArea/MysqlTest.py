__author__ = 'limitwh'
#coding=utf-8
import pymysql
import xml.etree.ElementTree as ET
from DBUtils.PooledDB import PooledDB
def GetDB(XMLfile):
    tree = ET.parse(XMLfile)
    root = tree.getroot()
    DBconfig={}
    for child in root:
        DBconfig['dbname']=child.attrib['name']
        for x in child:
            DBconfig[x.tag]=x.text
    return DBconfig

DBconfig=GetDB('test.xml')
print(DBconfig)
print(DBconfig['username'])
pool = PooledDB(pymysql,
                int(DBconfig['poolmin']),
                host=DBconfig['host'],
                user=DBconfig['username'],
                password=DBconfig['password'],
                db=DBconfig['dbname'],
                port=int(DBconfig['port']),
                charset=DBconfig['charset'])
conn = pool.connection()
SearchSql = "select * from goodstable"
# 使用cursor()方法获取操作游标
cur = conn.cursor()  
try:
    cur.execute(SearchSql)    #执行sql语句
    results = cur.fetchall()    #获取查询的所有记录  
    print("Gid","Gname","Gprice","Gnum")  
    #遍历结果  
    for row in results :  
        Gid = row[0]  
        Gname = row[1]  
        Gprice = row[2]  
        Gnum = row[3]
        print(Gid,Gname,Gprice,Gnum)  
except Exception as e:  
    raise e  
finally: #关闭连接
	#cur.close() 
    conn.close()