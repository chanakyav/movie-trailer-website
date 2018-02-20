#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import fresh_tomatoes
import media

""" Creating instances of the Movie class that contains movie title, storyline, poster image and trailer """

toy_story = media.Movie("Toystory",
                       "A story of a boy and his toys that come to life.",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

avengers = media.Movie("Avengers",
                       "A group of superheroes come together to fight aliens.",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

mad_max = media.Movie("Mad Max: Fury Road",
                      "A post apocalyptic desert wasteland where gasoline and water are scarce commodities.",
                      "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

the_big_short = media.Movie("The Big Short",
                            "Comedy drama about the financial crisis of 2007–2008 which was triggered by the United States housing bubble",
                            "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",
                            "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

john_wick = media.Movie("John Wick",
                        "a retired hitman seeking vengeance for the theft of his vintage car and the killing of his puppy, a gift from his recently deceased wife.",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=RllJtOw0USI")

# Creating a list with all the movie objects
movies = [toy_story, avatar, avengers, mad_max, the_big_short, john_wick]

# Opens the movie website with the "movies" list
fresh_tomatoes.open_movies_page(movies)

