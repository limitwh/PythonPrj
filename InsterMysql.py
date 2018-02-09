__author__ = 'limitwh'
#coding=utf-8
import pymysql
db=pymysql.connect(host="localhost",user="pytest",password="password",db="shopdb",port=3306,charset='utf8')
InsterSql="""INSERT INTO goodstable (Gname,Gprice,Gnum) VALUES('卤鸡蛋',2.0,45)"""
cur = db.cursor()  
print(InsterSql)
try:  
    sts=cur.execute(InsterSql) 
    if sts==1:
        print("Done")
    else:
        print("Failed")
    db.commit()
except Exception as e:  
    db.rollback()
    raise e     
finally:  
    cur.close()
    db.close()