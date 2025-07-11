class Song:
    """
    Represents a single song with title, artist, album, and year.
    """
    def __init__(self, title, artist, album, year, recording_filename):
        """
        Initializes a new Song object.

        Args:
            title (str): The title of the song.
            artist (str): The artist of the song.
            album (str): The album the song belongs to.
            year (int): The year the song was released.
        """
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
	self.recording_filename = recording_filename

    def display_song_info(self):
        """
        Prints the song's information in a readable format.
        """
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Album: {self.album}")
        print(f"Year: {self.year}")
	print(f"Recording Filename: {self.recording_filename}")
	

    def __repr__(self):
        """
        Provides a string representation of the Song object for debugging.
        """
        return f"Song(title='{self.title}', artist='{self.artist}', album='{self.album}', year={self.year}, recording_filename='{self.recording_filename}')"
