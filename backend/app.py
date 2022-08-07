# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, session, redirect
from secrets import token_urlsafe
import dbmodule.dbmodule as mongo


app = Flask(__name__)

# app.config['SECRET_KEY'] = token_urlsafe(16)

app.config['SECRET_KEY'] = "sadrtfgyhjuklihuftyufrksdfxd"


db = mongo.MongoDB()



# def index():
#     return "<h1>Sample index page</h1>"


@app.route("/get_rss", methods=["GET"])
def get_rss():
    if "user_id" in session:
        user_id = session["user_id"]

        # db.get_tasks_by_user(user_id)
    return redirect("/list_page")


@app.route("/list_page/delete/<task_id>")
def delete_task(task_id):
    if "user_id" in session:
        tasks = db.get_tasks_by_user()
        for task in tasks:
            if task["task_id"] == task_id:
                db.remove_task(_id=task_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form
        email = form.get("email")
        password = form.get("password")
        user = db.get_user(email)
        if user and db.check_login(email, password):
            session['user_id'] = user["_id"]

    return """<form action="" method="post">
            <p>Email: <input type=text required="required" name=email>
            <p>Password: <input type=text required="required" name=password>
            <p><input type=submit value="Submit">
        </form>"""


@app.route("/")
@app.route("/index")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/list_page")
def list_page():
    if "user_id" in session:
        user = db.get_user(_id=session["user_id"])
        tasks = db.get_tasks_by_user(user["_id"])
        print(tasks)
    return render_template("list_page.html")


@app.route("/statistic_page")
def statistic_page():
    return render_template("statistic_page.html")


@app.route("/group_page")
def group_page():
    return render_template("group_page.html")


@app.route("/pattern_page")
def pattern_page():
    if "user_id" in session:
        user = db.get_user(_id=session["user_id"])
        tasks = db.get_tasks_by_user(user["_id"])
        print(tasks)
    return render_template("pattern_page.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
