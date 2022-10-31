from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/forms.html")
def about():
    return render_template("forms.html")

# @app.route("/<username>/<int:post_id>")
# def main(username=None, post_id=None):
#     return render_template("index.html", name=username, post_id=post_id)

# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/blog/2020/dogs")
# def blog2():
#     return "this is my dog"
