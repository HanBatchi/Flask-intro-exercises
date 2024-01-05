from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def welcome_page():
  return "Welcome"


@app.route('/welcome/home')
def home_page():
  return "Welcome home"

@app.route('/welcome/back')
def back_page():
  return "Welcome back"


