#連線DB
from itertools import product
from dbConfig import conn, cur
import catalogue as cat
ProductList=cat.getList()
def Listhistory():
    #查詢
    sql="select id,product,date,price from cart order by id ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

#def delCartProduct(id):
    sql="delete from cart where id=%s;"#%s 讓你=前面的東西以他的數字或字串取代掉=24行的id
    cur.execute(sql,(id,))
    conn.commit()#寫入
    return True

def addCart(id,price):
    curprice="select price from bid where pid=%d;"%(id)
    cur.execute(curprice)
    curprice=cur.fetchall()
    currentprice=curprice[0][0]
    if price < int(currentprice):
        print(f"<p>{currentprice}</p>")
        return False
    sql="update bid set price='%d' where pid=%s;"%(price,id)
    cur.execute(sql)
    conn.commit()
    return True
#def checkoutcart():
    cartL=ListCart()
    for i in range(len(cartL)):
        for j in range(len(ProductList)):
            if cartL[i][0]==ProductList[j][0]:
                id=cartL[i][0]
                cartNums=cartL[i][2]
                sql="update catalogue set nums=nums-%d where id=%d;"%(cartNums,id)
                cur.execute(sql)
                conn.commit()
                sql="delete from cart where id=%d;"%(id)
                cur.execute(sql)
                conn.commit()#寫入
    return True
#def cacaluatecart():
    cartList=ListCart()
    totalprice=int(0)
    for i in range(len(cartList)):
        totalprice=int(cartList[i][2])*int(cartList[i][3])+totalprice
    return totalprice
