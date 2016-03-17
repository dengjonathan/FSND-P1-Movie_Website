# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:15:14 2016

@author: jonathandeng
"""

class Movie():  
    '''stores movie attributes within an instance of class Movie'''
    
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url= trailer_youtube_url
        
    def show_trailer(self):
        import webbrowser
        webbrowser.open(self.trailer)


        