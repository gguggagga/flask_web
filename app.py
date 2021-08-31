from flask import Flask , render_template
from data import Articles
import pymysql

db_connection = pymysql.connect(
	user = 'root',
        passwd  = '1234',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
        port=3307,
    	charset = 'utf8'
)

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/', methods=['GET', 'POST'])
def index():
    name="KIM"
    return render_template('index.html',data=name)

@app.route('/articles', methods=['GET', 'POST'])
def articles():
    # list_data = Articles()
    cursor = db_connection.cursor()
    sql = 'SELECT * FROM list;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    return render_template('articles.html', data = topics)

@app.route('/detail/<ids>')
def detail(ids):
    cursor = db_connection.cursor()
    sql = f'SELECT * FROM list where id ={int(ids)} ;'
    cursor.execute(sql)
    topic = cursor.fetchone()
    # list_data = Articles()
    # for data in topics:
    #     if data[0]==int(ids):
    #         article = data

    # return article 이것과 아래 render_template 의 차이로 템플릿, html의 유무를 설명    
    return render_template('article.html',article=topic)

if __name__ == '__main__':
    app.run( debug=True )



