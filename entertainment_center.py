import fresh_tomatoes
import media


#instances to describe movies

amadeus = media.Movie("Amadeus",
                         "A movie about the rivalry between Mozart and Salieri",
                         "https://upload.wikimedia.org/wikipedia/en/2/2f/Amadeusmov.jpg",
                         "https://www.youtube.com/watch?v=yIzhAKtEzY0")


forrestor = media.Movie("Finding Forrester", "Famous reclusive author mentors creative young writer",
                     "https://upload.wikimedia.org/wikipedia/en/1/16/Finding_forrester.jpg",
                     "https://www.youtube.com/watch?v=ziT9MlQjDjM")


kickass = media.Movie("Kick Ass",
                         "A movie about a teenage vigilante who takes on tye mob with some other real life superheroes",
                         "https://upload.wikimedia.org/wikipedia/en/3/30/Kick-Ass_film_poster.jpg",
                         "https://www.youtube.com/watch?v=rFpWpkxsVI8")

matrix = media.Movie("The Matrix",
                         "A movie about how the real is actual a computer program",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

pirates = media.Movie("Pirates of Silicon Valley",
                         "A movie about how Micorsoft and Apple got big",
                         "https://upload.wikimedia.org/wikipedia/en/3/30/Movieposterposv.jpg",
                         "https://www.youtube.com/watch?v=lEyrivrjAuU")

social = media.Movie("The Social Network",
                         "A movie about how Facebook started",
                         "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                         "https://www.youtube.com/watch?v=lB95KLmpLR4")






#list of my favorite movies
movies=[amadeus, forrestor, kickass, matrix, pirates, social]

#instance method that takes list of movies and produces webpage
#for movie trailers
fresh_tomatoes.open_movies_page(movies)
