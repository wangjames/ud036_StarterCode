import media
import fresh_tomatoes

# Starting point for generate_movies code.
# Retrieves list of movies from media module
# Calls the open_movies_page function from fresh_tomatoes to generate HTML.

if __name__ == "__main__":
    movie_data = media.create_list()
    fresh_tomatoes.open_movies_page(movie_data)