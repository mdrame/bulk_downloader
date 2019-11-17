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

    # I don't like Dictionary
        #adding all links to a list 
    urls = [ urlone, urltwo, urlthree, urlfour, urlfive ]
    
    #making sure requst is a GET before app can do any thing 
    if request.method == 'POST':
        #looping over list of url to get all possible indexes
        for i in range(0, len(urls)):
            if 'www.youtube.com' in urls[i]:
            # print(f"these are the {i}")
            # creating a instance of pytube libary and  making a call. Also saving it in a specific location using os.path so app will downlaod stuff to a spacific locaion for ever body that uses it.
                ytd = YouTube(f'{urls[i]}').streams.first().download('/Users/mohammeddrame/Downloads')
        
    else:
        print(" Method is POST ")

    return render_template('converting.html',  urls=urls)







# main module page 
if __name__ == "__main__":
    app.run(debug=True)

# Todo:
    # Error handle code
    # progress Hud
    # Specific Directory location to download file to