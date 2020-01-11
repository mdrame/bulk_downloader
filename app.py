from flask import Flask, render_template, redirect, request, url_for
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
    

# downlaoding music processing route
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

                                                                        # save to destination
                ytd = YouTube(f'{urls[i]}').streams.first().download('/Users/mohammeddrame/Downloads')
                # downloading given url
        
    else:
        print(" Method is POST ")

    return render_template('converting.html',  urls=urls)


# about route 
@app.route('/about')
def about():
    # display only 
    return render_template('about.html') #home page
    
# Render contant to github page
    

# pravicy route 
@app.route('/pp')
def pp():
    # display only 
    return render_template('privacypolicy.html') #home page
    




# main module page 
if __name__ == "__main__":
    app.run(debug=True)

# Todo:
    # Error handle code
    # progress Hud
    # Specific Directory location to download file to
