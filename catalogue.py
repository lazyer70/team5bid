#連線DB
from itertools import product
from dbConfig import conn, cur
def getList():
    #查詢
    sql="select pid,product,date,price,act from bid where act=1 order by pid ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
def Listact():
    #查詢
    sql="select pid,product,date,price,act from bid order by act  ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
##catalogueL=getList()
def showdetail(id):
    #查詢
    sql="select detail from bid where act=1 and pid=%s order by pid ;"%(id)
    cur.execute(sql)
    records = cur.fetchall()
    return records
##def delProduct(id):
    sql="delete from bid where id=%s;"#%s 讓你=前面的東西以他的數字或字串取代掉=24行的id
    cur.execute(sql,(id,))
    conn.commit()#寫入
    return True


def addProduct(product,date,price):
    sql="insert into bid (product,date,price,act) values (%s,%s,%s,%s);"
    cur.execute(sql,(product,date,price,1))
    conn.commit()
    return True
##def reviseProduct(id,name,Nums,price):
    if Nums>0:
        sql="update bid set nums=%d , product='%s',price='%d' where id=%s;"%(Nums,name,price,id)
    cur.execute(sql)
    conn.commit()
    return True
