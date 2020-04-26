import pymysql.cursors
from util import *

connection = util.connectdb.getConnection()
try:
    cursor = connection.cursor()
    # SQL
    sql = "SELECT * FROM employee"
    # Execute sql and pass - parameter
    cursor.execute(sql)

    # Loop
    for row in cursor:
        print(row)

except pymysql.Error as e:
    print("Error %s" % e.args[1])
finally:
    # ปิดการ connection
    connection.close()
