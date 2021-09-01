from typing import Counter
from flask import Flask , render_template , redirect, request
from data import Articles
import pymysql

db_connection = pymysql.connect(
	    user    = 'root',
        passwd  = '1234',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
    	charset = 'utf8'
)

app = Flask(__name__)

# @app.route('/hello')
# def hello_world():
#     return 'Hello World!'

@app.route('/', methods=['GET', 'POST'])
def index():
    name="KIM"
    return render_template('index.html',data=name)

@app.route('/register', methods=['GET', 'POST'])
def regitster():
    if request.method =='GET':        
        return render_template('register.html')
    else:
        username = request.form["username"]
        email = request.form["email"]
        password= request.form['password']
        cosur = db_connection.cursor()
        sql = f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}');"
        cosur.execute(sql)
        db_connection.commit()
        # return render_template('re_success.html')
        return redirect('/')
        

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

@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == "GET":
        return render_template('/add_article.html')
    else:
        title = request.form["title"]
        desc = request.form["desc"]
        author = request.form["author"]
        cursor = db_connection.cursor()
        sql = f"INSERT INTO list (title, description, author) VALUES ('{title}', '{desc}', '{author}');"
        cursor.execute(sql)
        db_connection.commit()
        return redirect('/articles')

@app.route('/edit_article/<ids>', methods=['GET', 'POST'])
def edit_article(ids):
    if request.method == 'GET':
        cursor = db_connection.cursor()
        sql = f'SELECT * FROM list WHERE id={int(ids)};'
        cursor.execute(sql)
        topic = cursor.fetchone()

        return render_template('/edit_article.html',article=topic)
    else:
        title = request.form["title"]
        desc = request.form["desc"]
        author = request.form["author"]

        cursor = db_connection.cursor()
        # sql = f"UPDATE list SET title= '{title}', description = '{desc}', author='{author}' WHERE (id = {int(ids)});"
        sql = f"UPDATE list SET title = '{title}', description = '{desc}', author = '{author}' WHERE (id = {int(ids)});"
        cursor.execute(sql)
        db_connection.commit()
        return redirect('/articles')

@app.route('/delete/<ids>', methods=['GET', 'POST'])
def delete(ids):
    cursor = db_connection.cursor()
    sql = f'DELETE FROM list WHERE (id = {ids});'
    cursor.execute(sql)
    db_connection.commit()
    return redirect('/articles')

if __name__ == '__main__':
    app.run( debug=True )



