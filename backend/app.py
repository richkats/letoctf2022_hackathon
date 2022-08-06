# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Sample index page</h1>"


def dashboard():
    return render_template("dashboard.html")


def list_page():
    return render_template("list_page.html")


def statistic_page():
    return render_template("statistic_page.html")


def group_page():
    return render_template("group_page.html")


def pattern_page():
    return render_template("pattern_page.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
