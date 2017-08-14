import media
import fresh_tomatoes

batman= media.Movie("Batman",
                    "A story of a boy and his actions against crime in his city",
                    "https://en.wikipedia.org/wiki/Batman#/media/File:Batman_Detective_Comics_Vol_2_1.png",
                    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

avatar= media.Movie("Avatar",
                    "A story of a soldier and other world",
                    "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

avengers= media.Movie("Avengers",
                    "A story of a super heros",
                    "https://en.wikipedia.org/wiki/The_Avengers_(2012_film)#/media/File:TheAvengers2012Poster.jpg",
                    "https://www.youtube.com/watch?v=4TcLu7n3PEg")


movies = [batman,avatar,avengers]

fresh_tomatoes.open_movies_page(movies)

#print(batman.storyline)

#batman.show_trailer()
