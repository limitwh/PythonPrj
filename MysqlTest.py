__author__ = 'limitwh'
#coding=utf-8
import pymysql
db=pymysql.connect(host="localhost",user="pytest",password="password",db="shopdb",port=3306,charset='utf8')
SearchSql = "select * from goodstable"
# 使用cursor()方法获取操作游标
cur = db.cursor()  
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
    db.close()     