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
 

    ytd = YouTube('https://www.youtube.com/watch?v=SpQ0Xh7J4_4&list=PLKIjVmbmuiOFIFYo8zX5Pq3YGhPz00JOC&index=2').streams.first().download('/Users/mohammeddrame/Downloads') // where you want the downlad to go
    if ytd:
        print("VIDEO DOWNLOADED SUCCESSFULLY")
    else:
        print(' Let user know process fail ')


    return render_template('converting.html',  url=url)



@app.route('/downloading') 
def downloading(): 
    pass







# main module page 
if __name__ == "__main__":
    app.run(debug=True)
