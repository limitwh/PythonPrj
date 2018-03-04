PythonPrj
===
需要的Python包:
---

*requests
*BeautifulSoup
*pymysql

* 0.DB准备
	* 执行DB.sql下的DDL，建立数据库，表，索引和视图

* 1.初始化
	* A.从JD的URL里取得每个商品的URL和ID
		* ItemUrl=GetItemFromUrl("https://list.jd.com/list.html?cat=9987,653,655&page=4")
	* B.For循环逐个从JD移动网页取得商品的价格
		* temList=[]
			* for ItemID in ItemUrl:
				* time.sleep(0.15)
				* ItemName=(GetName(ItemUrl[ItemID]))
				* ItemPrice=(GetMobPrice(ItemID))
				* ItemList.append([ItemID,ItemUrl[ItemID],ItemName,ItemPrice])
	* C.插入DB
		* InsertDB(ItemList)
	* D.将Current表同步到History表
		* UpdateHis()

* 2.日常更新操作
	* A.更新Current表
		* UpdateCur()
	* B.将Current表同步到History表
		* UpdateHis()