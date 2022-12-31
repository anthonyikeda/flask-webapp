""" Entry point to application """
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    """ Index page """
    return render_template("index.html", title="First Python Application", name="Person A")

@app.route("/input")
def info_collect():
    """ Collect some basic data """
    return render_template("input.html", message="Please enter your details")

@app.route("/record", methods=['POST'])
def info_submission():
    """ Read the submitted data """
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    age = request.form["age"]
    print(f'User is {firstname}, {lastname} and their age is {age}')
    return render_template("input.html", message="Done")
