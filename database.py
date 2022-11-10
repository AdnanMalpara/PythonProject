
import pymysql

con = None
cursor = None

def dbconnect():
    global con, cursor
    con = pymysql.connect(host='localhost',
                    user='root',
                    password='',
                    database='project')
    cursor = con.cursor()    

def dbdisconnect():
    cursor.close()
    con.close()

def insertrecord(id,name,location,companyname,post):
    dbconnect()
    query = f'insert into employee values({id},"{name}","{location}","{companyname}","{post}")'
    cursor.execute(query)
    con.commit()
    dbdisconnect()

def readall():
    dbconnect()
    query = 'select * from employee'
    cursor.execute(query)
    data = cursor.fetchall()
    #print(data)
    dbdisconnect()
    return data

def readbyid(id):
    dbconnect()
    query = f'select * from employee where id={id}'
    cursor.execute(query)
    data = cursor.fetchone()
    dbdisconnect()
    return data

def updaterecord(data):
    dbconnect()
    query = f'update employee set name="{data[1]}", location="{data[2]}",companyname="{data[3]}",post="{data[4]}" where id={data[0]}'
    cursor.execute(query)
    con.commit()
    dbdisconnect()

def deleterecord(id):
    dbconnect()
    query = f'delete from employee where id={id}'
    cursor.execute(query)
    con.commit()
    dbdisconnect()
