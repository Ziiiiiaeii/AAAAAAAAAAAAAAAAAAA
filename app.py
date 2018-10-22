from flask import Flask, render_template


app = Flask(__name__)


answers = []
infile = open('answers.txt', 'r')
for line in file:
  answers.append(line.strip())


@app.route('/')
def index():
    return render_template("home.html", newAnswer)


@app.route('/about')
def about():
    return render_template("about.html")


app.run()
