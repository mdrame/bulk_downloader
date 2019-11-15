from flask import Flask, render_template, redirect, request
import requests
import os 
from pytube import YouTube


# Created by Mohammed Draem 
# Computer software engineer student at Make School, San Francisco , CA
# Personal Project 



app = Flask(__name__)






# home route 
@app.route('/')
def index():
    # display only 
    return render_template('index.html') #home page
    

@app.route('/converting', methods=['GET', 'POST'])
def converting_url():

    ''' create a list and append form input as it index '''
    #urls from form
    urlone = request.form.get("urlone")
    urltwo = request.form.get("urltwo")
    urlthree = request.form.get("urlthree")
    urlfour = request.form.get("urlfour")
    urlfive = request.form.get("urlfive")

    
    # this is usually right behind the url of API address
    # I don't like Dictionary
    url = [ urlone, urltwo, urlthree, urlfour, urlfive ]

    # write downloading code here
 
    # creating a object making a call and saving it in a specific location
    # ytd = YouTube(f'{urlone}').streams.first().download('/Users/mohammeddrame/Downloads')
   


    return render_template('converting.html',  url=url)







# main module page 
if __name__ == "__main__":
    app.run(debug=True)

# Todo:
    # Error handle code
    # progress Hud