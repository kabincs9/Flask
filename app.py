from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # to use jinja for name like if there is value of name in greet
        return render_template("greet.html", name=request.form.get("name"))
    return render_template("index.html")
