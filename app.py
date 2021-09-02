import re
from typing import Counter
from flask import Flask , render_template , redirect, request, session, url_for
from flask.typing import ResponseValue
from pymysql import NULL, cursors
# from data import Articles
from passlib.hash import pbkdf2_sha256
import pymysql
from functools import wraps
from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:1234@cluster0.4dhoo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.gnagnam
db_user = client.users

list = db.list
users = db_user.users

app = Flask(__name__)
app.config['SECRET_KEY']= 'gangnam'
# print(len(session))
db_connection = pymysql.connect(
	    user    = 'root',
        passwd  = '1234',
    	host    = '127.0.0.1',
    	db      = 'gangnam',
    	charset = 'utf8'
)
# @app.route('/hello')
# def hello_world():
#     return 'Hello World!'

def is_logged_in(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'is_logged' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

def is_admin(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if session['email'] == '2@naver.com':
            return f(*args, **kwargs)
        else:
            return redirect(url_for('articles'))
    return wrap



@app.route('/', methods=['GET', 'POST'])
def index():
    name="KIM"
    return render_template('index.html',data=name, user=session)


# 빈데이터를 넣지 않으려면 폼체크 구성하기
@app.route('/register', methods=['GET', 'POST'])
def regitster():
    if request.method =='GET':        
        return render_template('register.html')
    else:
        username = request.form["username"]
        email = request.form["email"]
        password= pbkdf2_sha256.hash(request.form['password'])

        users.insert_one({"username":username,"email":email,"password":password})
        cursor = db_connection.cursor()
        sql_1 = f"select * from users where email='{email}'"
        cursor.execute(sql_1)
        user = cursor.fetchone()
        #print(user) email이 db안에 존재하는지 확인
        if user == None:
            sql = f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}');"
            cursor.execute(sql)
            db_connection.commit()
            # return render_template('re_success.html')
            return redirect('/')
        else : 
            return redirect('/register')

@app.route('/login', methods =['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        email = request.form["email"]
        password = request.form["password"]
        sql1 = f"select * from users where email = '{email}'"
        cursor = db_connection.cursor()
        cursor.execute(sql1)
        user = cursor.fetchone()
        print(user)
        if user == None:
            print(user)
            return redirect('/login')
        else:
            result=pbkdf2_sha256.verify(password,user[3])
            if result == True :
                session['id']=user[0]
                session['username']=user[1]
                session['email']=user[2]
                session['date']=user[4]
                session['is_logged']=True
                print(session)
                return redirect('/')
            else : 
                return redirect('/login')

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect('/')



@app.route('/articles', methods=['GET', 'POST'])
def articles():
    # list_data = Articles()
    cursor = db_connection.cursor()
    sql = 'SELECT * FROM list;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    return render_template('articles.html', data = topics, user=session)

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
    return render_template('article.html',article=topic, user=session)

@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    if request.method == "GET":
        return render_template('/add_article.html',user=session)
    else:
        title = request.form["title"]
        desc = request.form["desc"]
        author = request.form["author"]
        list.insert_one({"title":title,"desc":desc,"author":author},tls =True,tlsAllowInvalidCertificates=True)
        cursor = db_connection.cursor()
        sql = f"INSERT INTO list (title, description, author) VALUES ('{title}', '{desc}', '{author}');"
        cursor.execute(sql)
        db_connection.commit()
        return redirect('/articles')

@app.route('/edit_article/<ids>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(ids):
    if request.method == 'GET':
        cursor = db_connection.cursor()
        sql = f'SELECT * FROM list WHERE id={int(ids)};'
        cursor.execute(sql)
        topic = cursor.fetchone()

        return render_template('/edit_article.html',article=topic,user=session)
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
@is_logged_in
@is_admin
def delete(ids):
    cursor = db_connection.cursor()
    sql = f'DELETE FROM list WHERE (id = {ids});'
    cursor.execute(sql)
    db_connection.commit()
    return redirect('/articles')

if __name__ == '__main__':
    app.run( debug=True )