import media
import fresh_tomatoes

Up= media.Movie("Up!",
                  "Storyline",
                  "https://upload.wikimedia.org/wikipedia/en/0/05/Up_(2009_film).jpg",
                  "https://www.youtube.com/watch?v=pkqzFUhGPJg")

GodFather = media.Movie("GodFather",
                     "Storyline",
                     "http://vignette1.wikia.nocookie.net/godfather/images/2/2c/The_Godfather_Game.jpeg/revision/latest?cb=20131009061406",
                     "https://www.youtube.com/watch?v=sY1S34973zA")

silicon_valley = media.Movie("Pirates of Silicon Valley",
                             "A biographical look at the men who made the world of technology what it is today",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Movieposterposv.jpg/250px-Movieposterposv.jpg",
                             "https://www.youtube.com/watch?v=lEyrivrjAuU")

Scarface = media.Movie("Scarface",
                             "Storyline",
                             "https://upload.wikimedia.org/wikipedia/en/f/f8/ScarfaceMPR.jpg",
                             "https://www.youtube.com/watch?v=oSMOEKEcjqk")

ShawshankRedemption = media.Movie("Shawshank Redemption",
                             "Storyline",
                             "http://vignette2.wikia.nocookie.net/filmguide/images/c/cb/The_Shawshank_Redemption.jpg/revision/latest?cb=20120122172923",
                             "https://www.youtube.com/watch?v=K_tLp7T6U1c")

BladeRunner = media.Movie("Blade Runner",
                             "Storyline",
                             "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                             "https://www.youtube.com/watch?v=gCcx85zbxz4")


movies = [Up, GodFather, silicon_valley, Scarface, ShawshankRedemption, BladeRunner]

fresh_tomatoes.open_movies_page(movies)
