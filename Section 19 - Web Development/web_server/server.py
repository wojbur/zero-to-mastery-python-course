import mimetypes
import os
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/<username>/<int:post_id>")
def main(username=None, post_id=None):
    return render_template("index.html", name=username, post_id=post_id)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/blog/2020/dogs")
def blog2():
    return "this is my dog"
