
from sqlite3 import connect
from flask import Flask, jsonify
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from mysql.connector import pooling
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key = "the key"
app.config['JSON_AS_ASCII'] = False
connection_pool = pooling.MySQLConnectionPool(pool_name="mysql_pool",
                                              pool_size=5,
                                              pool_reset_session=True,
                                              host="localhost",
                                              user="root",
                                              password="123456",
                                              database="website")
mydb = connection_pool.get_connection()


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM member WHERE username = %s", (username,))
    result = mycursor.fetchone()
    # print(result)
    if username == "" or password == "":
        err_code = "請輸入帳號、密碼"
        return redirect(url_for('error', message=err_code))
    elif result:
        for i in result:
            check_pwd = result[3]
            name = result[1]
            if check_password_hash(check_pwd, password):
                session["username"] = username
                session["name"] = name
                return redirect("/member/")
            else:
                err_code = "帳號、密碼輸入錯誤"
                return redirect(url_for('error', message=err_code))
    else:
        err_code = "帳號、帳號輸入錯誤"
        return redirect(url_for('error', message=err_code))


@ app.route("/signup/", methods=["POST"])
def signup():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        hashed_pwd = generate_password_hash(password).encode("UTF-8")
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT username FROM member WHERE username = %s", (username,))
        account = mycursor.fetchone()
        if account:
            data = "帳號已經被註冊"
            return redirect(url_for('error', message=data))
        elif not name or not username or not password:
            data = "請重新檢查是否已填入正確資訊"
            return redirect(url_for('error', message=data))
        else:
            mycursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)",
                             (name, username, hashed_pwd))
            mydb.commit()
            session['name'] = request.form['name']
            session['username'] = request.form['username']
            return redirect(url_for("member"))


@ app.route("/member/", methods=["POST", "GET"])
def member():
    if 'username' in session:
        data = session["username"]
        name = session["name"]
        return render_template("member.html", username=data, name=name)
    return redirect("/")


@app.route("/api/members", methods=["GET"])
def members():
    data = request.args.get('username', '')
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM member WHERE username = %s", (data,))
    result = mycursor.fetchone()
    data = {}
    if result:
        data['id'] = result[0]
        data['name'] = result[1]
        data['username'] = result[2]
        return jsonify({'data': data})
    else:
        return jsonify({'data': None})


@ app.route("/error/")
def error():
    data = request.args.get('message', '')
    return render_template('error.html', err_message=data)


@ app.route("/signout", methods=["GET"])
def signout():
    session.pop('username', None)
    return render_template("index.html")


app.run(port=3000, debug=True)
