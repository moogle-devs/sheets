from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("edit.html")

@app.route('/edit')
def edit():
  return render_template("edit.html")

app.run('0.0.0.0', port=81)
