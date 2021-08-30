from flask import Flask
from flask.templating import render_template
from data import Articles

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

# @ < 데코레이터 
@app.route('/',methods=['GET','POST'])
def index():
    name="KIM"
    return render_template('index.html',data = name)

@app.route('/articles',methods=['GET','POST'])
def articles():
    list_data = Articles()
    return render_template('articles.html',data = list_data)

@app.route('/articles2',methods=['GET','POST'])
def articles2():
    list_data = Articles()
    return render_template('articles2.html',data = list_data)

@app.route('/detail/<ids>')   # parameters 처리 > 선택에 따라 바뀌는 
def detail(ids):
    return

if __name__ == '__main__':
    app.run(debug=True)
