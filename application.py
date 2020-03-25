from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def projetcorrection():
    return render_template('projetcorrection.html')