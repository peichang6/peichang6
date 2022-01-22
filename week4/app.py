
from operator import truediv
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key = "the key"


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    input_name = request.form["username"]
    input_password = request.form["password"]
    if input_name == "test" and input_password == "test":
        session["username"] = input_name
        return redirect("/member/")
    elif input_name == "" or input_password == " ":
        err_code = "請輸入帳號、密碼"
        return redirect(url_for('error', message=err_code))
    else:
        err_code = "帳號、或密碼輸入錯誤"
        return redirect(url_for('error', message=err_code))


@app.route("/member/")
def member():
    if 'username' in session:
        # print(session)
        return render_template("member.html")
    return redirect("/")


@app.route("/error/")
def error():
    data = request.args.get('message', '')
    return render_template('error.html', err_message=data)


@app.route("/signout", methods=["GET"])
def signout():
    session.pop('username', None)
    return render_template("index.html")


app.run(port=3000)
