# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Sample index page</h1>"


def dashboard():
    return "<h1>dashboard</h1>"


def templates():
    return "<h1>templates</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
