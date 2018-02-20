#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import webbrowser

class Movie():
    """ This class provides a way to store movie related information 
    
    Attributes:
        VALID_RATINGS: MPAA ratings for movies.
    """
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Inits Movie class with a movie's title, storyline, poster image, and trailer """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """ Opens up the youtube trailer of an instance of Movie class in a broswer """
        webbrowser.open(self.trailer_youtube_url)
        

        