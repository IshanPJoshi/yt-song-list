from flask import Flask, render_template, request
import math
import db

app = Flask(__name__)

@app.before_first_request
def initialize():
    db.setup()
    
@app.route('/')
def default():
    pageNum = max(request.args.get('page', 1, type=int), 1)
    totalPages = math.ceil(db.get_song_count()/100)
    songs = db.get_songs(page=pageNum-1)
    return render_template('main.html', songs=songs, pageNum=pageNum, totalPages = totalPages)