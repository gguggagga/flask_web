<<<<<<< HEAD
from flask import Flask , render_template , redirect
=======
from flask import Flask , render_template
>>>>>>> 402e4cad16edf9deadbdb830e6e37600b2d75480
from data import Articles
import pymysql

db_connection = pymysql.connect(
<<<<<<< HEAD
	    user    = 'root',
        passwd  = '1234',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
=======
	user = 'root',
        passwd  = '1234',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
        port=3307,
>>>>>>> 402e4cad16edf9deadbdb830e6e37600b2d75480
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
<<<<<<< HEAD
    # list_data = Articles()
    cursor = db_connection.cursor()
    sql = f'SELECT * FROM list WHERE id={int(ids)};'
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    # for data in list_data:
    #     if data['id']==int(ids):
    #         article = data

    return render_template('article.html',article=topic)

@app.route('/delete/<ids>', methods=['GET', 'POST'])
def delete(ids):
    cursor = db_connection.cursor()
    sql = f'DELETE FROM list WHERE (id = {ids});'
    cursor.execute(sql)
    db_connection.commit()
    return redirect('/articles')

=======
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

>>>>>>> 402e4cad16edf9deadbdb830e6e37600b2d75480
if __name__ == '__main__':
    app.run( debug=True )



