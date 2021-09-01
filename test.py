import pymysql

db_connection = pymysql.connect(
	user    = 'root',
        passwd  = '1234',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
        port = 3307,
    	charset = 'utf8'
)
cursor = db_connection.cursor()
sql = 'SELECT * FROM list;'
cursor.execute(sql)
topics = cursor.fetchall()
print(topics)