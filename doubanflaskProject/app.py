from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/index')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/movie')
def movie():
    con = mysql.connector.connect(
        host='localhost', port=3306,
        user='root', password='root',
        database='douban'
    )
    cursor = con.cursor()
    datalist = []
    sql = "select * from movie250"
    data = cursor.execute(sql)
    datalist = cursor.fetchall()
    # for item in data:
    #     datalist.append(item)
    cursor.close()
    con.close()
    return render_template("movie.html", movies=datalist)


@app.route('/score')
def score():
    con = mysql.connector.connect(
        host='localhost', port=3306,
        user='root', password='root',
        database='douban'
    )
    datalist = []
    a_score = []
    num = []
    cursor = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cursor.execute(sql)
    datalist = cursor.fetchall()
    for item in datalist:
        a_score.append(item[0])
        num.append(item[1])
    cursor.close()
    con.close()
    return render_template("score.html",score=a_score,num=num)


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
