from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
  return render_template('welcome.html')

@app.route('/home')
def home():
  return render_template('home.html')

if __name__ == '__main__':

  app.debug = True
  app.run(host='0.0.0.0')


