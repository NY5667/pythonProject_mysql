import mysql.connector

cnx = mysql.connector.connect(user='root', password='1',
                              host='127.0.0.1',
                              database='employees')
cnx.close()