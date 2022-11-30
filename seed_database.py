"""""""""Script to seed database."""
import os
import json
from random import choice,  randintfrom 
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create.all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movie_list = []
for movie in movie_data:
    title, overview, poster_path = (movie['title'], movie['overview'], movie['poster_path'],)
    release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")
    movie_list.append(movie)
