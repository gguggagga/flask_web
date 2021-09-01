# import pymysql

# db_connection = pymysql.connect(
# 	user    = 'root',
#         passwd  = '1234',
#     	host    = '127.0.0.1',
#     	db      = 'gangnam',
#         port = 3307,
#     	charset = 'utf8'
# )
# cursor = db_connection.cursor()
# sql = 'SELECT * FROM list;'
# cursor.execute(sql)
# topics = cursor.fetchall()
# print(topics)
from passlib.hash import pbkdf2_sha256

hash = pbkdf2_sha256.hash("1234")
print(hash)

result = pbkdf2_sha256.verify("1234",hash)
print(result)
# app.config['SECRET_KEY'] = 'I am your bro'
# app.config['BCRYPT_LEVEL'] = 10