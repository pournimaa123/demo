import mysql.connector
def change():
    con=mysql.connector.connect(host="localhost",user="root",password="system",database="student")
    try:
        str="alter table emp add( salary int )"
        cur=con.cursor()
        cur.execute(str)
        con.commit()
        cur.close()
        con.close()
    except:
        print("error occured")
change()
 
