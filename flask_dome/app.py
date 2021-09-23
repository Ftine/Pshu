from flask import Flask,render_template,request
import datetime

app = Flask(__name__)


# 路由解析，通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def hello_world():  # put application's code here
#     return '吱吱吱种子,hello world'
@app.route('/index')
def hello():
    return '你好'

# 通过用户访问的路径，进行传参
# @app.route('/user/<name>')
# def welcome(name):
#     return '靓仔你好%s' % name

@app.route('/user/<int:id>')
def welcome(id):
    return '靓仔你好你id%s' % id

@app.route('/')
def index():
    time = datetime.date.today()
    name = ['xiaozhang','Ab','阿门']
    task = {"洗衣服":"30min","扫地":"10min"}
    return render_template('index.html',var=time,list=name,task=task)

@app.route('/test/register')
def register():
    return render_template("register.html")

# 接受表单提交要post，给定方法
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html",result=result)

if __name__ == '__main__':
    app.run()
