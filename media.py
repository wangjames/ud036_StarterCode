
# Returns a hardcoded list of Movie objects with example movies

def create_list():
    raw_data = [Movie("Inception", 
                      "https://goo.gl/L2cHYS",
                      "https://www.youtube.com/watch?v=8hP9D6kZseM"),
                Movie("Interstellar", 
                      "https://goo.gl/zhjb6X",
                      "https://www.youtube.com/watch?v=zSWdZVtXT7E"),
                Movie("Michael Clayton",
                       "https://goo.gl/UIpx2v",
                       "https://www.youtube.com/watch?v=5kJRYBhG43Q"),
                Movie("Sicario",
                       "https://goo.gl/dXkY7i",
                       "https://www.youtube.com/watch?v=sR0SDT2GeFg"),
                Movie("Midnight in Paris",
                       "https://goo.gl/RbBT8s",
                       "https://www.youtube.com/watch?v=BYRWfS2s2v4"),
                Movie("Jiro Dreams of Sushi",
                      "https://goo.gl/ZQK4Fb",
                      "https://www.youtube.com/watch?v=I1UDS2kgqY8")]
    return raw_data

# Movie object specification
   
class Movie(object):
    
    # Constructor definition that defines the class variables of the object.
    
    def __init__(self, movie_name, image_url, youtube_id):
        self.title = movie_name
        self.poster_image_url = image_url
        self.trailer_youtube_url = youtube_id

