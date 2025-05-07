from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route('/wishes')
def wishes():
    return render_template('wishes.html')

@app.route('/plans')
def plans():
    return render_template('plans.html')

@app.route('/ps')
def ps():
    return render_template('ps.html')

@app.route('/sweet')
def sweet():
    return render_template('sweet.html')