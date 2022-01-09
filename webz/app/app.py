from flask import Flask, request, template_rendered
import time
import smtplib
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/hosting')
def host():
    return render_template('host.html')

@app.route('/webs')
def webs():
    return render_template('webs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)