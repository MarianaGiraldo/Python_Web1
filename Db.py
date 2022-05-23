import pymysql 

def mysqlConnect():
    conn = pymysql.Connect(
    host = 'localhost',
    port = 3306,
    user = 'user',
    password = 'developer',
    db = 'fasterbus_db')
    return conn
