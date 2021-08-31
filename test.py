import pymysql

db_connection = pymysql.connect(
<<<<<<< HEAD
	    user    = 'root',
        passwd  = '1234',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
=======
	user    = 'root',
        passwd  = '1234',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
        port = 3307,
>>>>>>> 402e4cad16edf9deadbdb830e6e37600b2d75480
    	charset = 'utf8'
)

cursor = db_connection.cursor()

sql = 'SELECT * FROM list;'

cursor.execute(sql)

topics = cursor.fetchall()

<<<<<<< HEAD
print(topics)

=======
print(topics)
>>>>>>> 402e4cad16edf9deadbdb830e6e37600b2d75480
