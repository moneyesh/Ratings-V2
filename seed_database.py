"""""""""Script to seed database."""
import os
import json
from random import choice,  randint  
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movie_list = []
for movie in movie_data:
    title, overview, poster_path = (movie['title'], movie['overview'], movie['poster_path'],)
    release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d") 
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movie_list.append(db_movie)
model.db.session.add_all(movie_list)
model.db.session.commit()



#Create an user:
for n in range(10):
    email = f'user{n}@test.com' 
    password = 'test'

    user = crud.create_user(email, password)
    model.db.session.add(user) # adding user to model.py

    #Create 10 fakes ratings for user
    for i in range(10):
        choose_movie = choice(movie_list) #Choose random movie from movie_list
        score = randint(1, 5) #Choose random score from 1-5

        rating = crud.create_rating(user, choose_movie, score)
        model.db.session.add(rating)

model.db.session.commit()
