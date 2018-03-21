import media
import fresh_tomatoes

toy_story = media.Movie("Up!",
                  "Storyline",
                  "https://upload.wikimedia.org/wikipedia/en/0/05/Up_(2009_film).jpg",
                  "https://www.youtube.com/watch?v=pkqzFUhGPJg")

avatar = media.Movie("GodFather",
                     "Storyline",
                     "http://vignette1.wikia.nocookie.net/godfather/images/2/2c/The_Godfather_Game.jpeg/revision/latest?cb=20131009061406",
                     "https://www.youtube.com/watch?v=sY1S34973zA")

silicon_valley = media.Movie("Pirates of Silicon Valley",
                             "A biographical look at the men who made the world of technology what it is today",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Movieposterposv.jpg/250px-Movieposterposv.jpg",
                             "https://www.youtube.com/watch?v=lEyrivrjAuU")

ratatouille = media.Movie("Scarface",
                             "Storyline",
                             "https://upload.wikimedia.org/wikipedia/en/f/f8/ScarfaceMPR.jpg",
                             "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Shawshank Redemption",
                             "Storyline",
                             "http://vignette2.wikia.nocookie.net/filmguide/images/c/cb/The_Shawshank_Redemption.jpg/revision/latest?cb=20120122172923",
                             "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Blade Runner",
                             "Storyline",
                             "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                             "https://www.youtube.com/watch?v=PbA63a7Hb0")


movies = [toy_story, avatar, silicon_valley, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)
