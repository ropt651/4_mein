from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def main_page():
    number = random.randint(1, 100)
    return render_template("index.html", number=number)

@app.route("/ds1")
def ds1_page():
    return render_template("ds1/index.html")

@app.route("/ds2")
def ds2_page():
    return render_template("ds2/index.html")

@app.route("/ds3")
def ds3_page():
    return render_template("ds3/index.html")

@app.route("/sekiro")
def sekiro_page():
    return render_template("sekiro/index.html")

@app.route("/bloodborne")
def bloodborne_page():
    return render_template("bloodborne/index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)