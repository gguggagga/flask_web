import pymysql

db_connection = pymysql.connect(
	user    = 'root',
        passwd  = 'APM_Setup',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
    	charset = 'utf8'
)

cursor = db_connection.cursor()

sql = 'SELECT * FROM list;'

cursor.excute(sql)

topics = cursor.fetchall()

print(topics)