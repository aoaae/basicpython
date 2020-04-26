import pymysql.cursors
from util import *

connection = util.connectdb.getConnection()
try:
    cursor = connection.cursor()
    # SQL
    sql = "INSERT INTO employee(emp_no,emp_name,emp_salary) VALUES(%s,%s,%s)"
    # Execute sql and pass - parameter
    cursor.execute(sql, ('1', 'Suksawat', '20000'))
    connection.commit()

    print("Create new employee success")
except pymysql.Error as e:
    print("Error %s" % e.args[1])
finally:
    # ปิดการ connection
    connection.close()
