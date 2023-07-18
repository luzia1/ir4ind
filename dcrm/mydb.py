import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'greenauto2664'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE greenauto")

print('all done')