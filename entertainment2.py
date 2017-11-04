import media2
import fresh_tomatoes2

toy_story = media2.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "John Lasseter")

avatar = media2.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "James Cameron")

wall_e = media2.Movie("Wall-E",
                     "The love story between two robots trying to save the Earth",
                     "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                     "https://www.youtube.com/watch?v=5RcNwlq7JSw",
                     "Andrew Stanton")

about_time = media2.Movie("About Time",
                          "A young man who can travel in time and tries to find his love",
                          "https://upload.wikimedia.org/wikipedia/en/8/88/About_Time_Poster.jpg",
                          "https://www.youtube.com/watch?v=u2PUMA6nFWk",
                          "Richard Curtis")

harry_potter = media2.Movie("Harry Potter and the Deathly Hallows Part 2",
                            "The final battle between Dark Lord and Harry Potter",
                            "https://goo.gl/NympRn",
                            "https://www.youtube.com/watch?v=mObK5XD8udk",
                            "David Yates")

lotr = media2.Movie("The Lord of the Rings: The Return of the King",
                    "The battle between the good and evil forces for a ring to rule them all",
                    "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                    "https://www.youtube.com/watch?v=Wmm5SNcjLvo",
                    "Peter Jackson")

rick_and_morty = media2.TV_Series("Rick and Morty",
                                  "Adventures of mad scientist and his grandson",
                                  "https://upload.wikimedia.org/wikipedia/en/3/32/Rick_and_Morty_opening_credits.jpeg",
                                  "https://www.youtube.com/watch?v=WNhH00OIPP0",
                                  "3 Seasons (2013 - )")

black_mirror = media2.TV_Series("Black Mirror",
                                "A dystopian tv series with dark and satirical themes that examine modern society",
                                "https://upload.wikimedia.org/wikipedia/en/2/24/BlackMirrorTitleCard.jpg",
                                "https://www.youtube.com/watch?v=jROLrhQkK78",
                                "3 Seasons (2011 - )")

seinfeld = media2.TV_Series("Seinfeld",
                            "An American sitcom about nothing",
                            "http://www.123posters.com/images/movie/f-seinfeld1.jpg",
                            "https://www.youtube.com/watch?v=SOsbYJ4CfTA",
                            "9 Seasons (1989 - 1998 )")

movies = [toy_story, avatar, wall_e, about_time, harry_potter, lotr]
tvseries = [rick_and_morty, black_mirror, seinfeld]
fresh_tomatoes2.open_movies_page(movies, tvseries)
