import webbrowser

class Video():
    """This class stores information about the movies and the TVseries"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ initialize instance of class Video"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens youtube link for the trailers """
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_director):
        """ initialize instance of class Movie"""
        Video.__init__(self, movie_title, movie_storyline, poster_image, trailer_youtube)
        self.director = movie_director

class TV_Series(Video):
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, tv_series_seasons):
        """ initialize instance of class TV_series"""
        Video.__init__(self, movie_title, movie_storyline, poster_image, trailer_youtube)
        self.seasons = tv_series_seasons
