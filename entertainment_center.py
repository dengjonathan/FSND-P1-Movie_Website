# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:19:47 2016

@author: jonathandeng

Uses constructor in media.py to create instances of the Movie class and append\
them to a list.

These movies are then displayed on an html page with the ability to open their\
trailers on youtube.
"""
import media
import fresh_tomatoes

movies = []


def create_movie(title, storyline, poster_image_url, trailer_youtube_url):
    """creates new instance of class Movie and appends the instance to the\
    list movies
    """
    movie = media.Movie(title, storyline, poster_image_url, trailer_youtube_url)
    movies.append(movie)
    return movie

# adding movies to webpage

y_tu_mama_tambien = create_movie('Y Tu Mama Tambien',
                                 'Two boys take a woman to a beach',
                                 'https://loftcinema.com/files/2015/03/y-tu-\
                                 mama-tambien-movie-poster-2002-1020213965.jpg',
                                 'https://www.youtube.com/watch?v=3Qg6n7V3kO4')

shawshank_redemption = create_movie('The Shawshank Redemption',
                                    'Two guys get out jail',
                                    'https://t0.gstatic.com/images?q=tbn:ANd9Gc\
                                    SkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrun\
                                    A1XjNTSKm',
                                    'https://www.youtube.com/watch?v=6hB3S9bI\
                                    aco')

trainspotting = create_movie('Trainspotting',
                             'Some friends in Scotland attempt to quit heroin',
                             'https://ok2disconnectportfolio.files.wordpress.\
                             com/2011/05/trainspotting-poster.jpg',
                             'www.youtube.com/watch?v=GmQqhuKmECc')
# using open_movies_page function in module fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
