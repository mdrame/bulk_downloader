from flask import Flask, render_template, redirect, request
import requests
import os 


# Created by Mohammed Draem 
# Computer software engineer student at Make School, San Francisco , CA
# Personal Project 



app = Flask(__name__)




mail = Mail(app) # mail instance / object 


# home route 
@app.route('/')
def index():
    
    return render_template('index.html') #home page
    








# main module page 
if __name__ == "__main__":
    app.run(debug=False) 
