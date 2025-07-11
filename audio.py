import os
import pickle
import librosa
import numpy as np

class AudioDatabase:
    ##initializes database based on path
    def _init_(self, db_path = "data"): ##what would this path be?
        self.db_path = db_path
        self.database = {}
        self.load_database()
    
    ##should check if database exists and loads it with pickel
    def load_database(self):
        if os.path.exists(self.db.path):
            with open(self.db_path, "rb") as f:
                self.database = pickle.load(f)
            print(f"Database loaded from {self.db_path}")
        else: 
            print(f"No database found at {self.db_path}")
    
    ##creates database, 
    def save_database(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok = True)
        with open(self.db_path, "wb") as f:
            pickle.dump(self.database, f)
        print("saved")

##prints all songs in database
    def list_songs(self): 
        if not self.database:
            print("No songs in database.")
            return 
        for i, (key, song) in enumerate(self.database.items(), 1): 
            print(f"{i}. {song['title']} by {song['artist']}")

    ##retrieves song data based on title + artist
    def get_song_data(self, title, artist): ##are we using title and artist as keys?   
        key = self._make_key(title, artist)
        return self.database.get(key, {})
    
    def add_song(self, title, artist, filepath):
        key = self._make_key(title, artist)
        if key in self.database:
            print(" Song already exists.")
            return

        soundwave, frequencies = self.extract_audio_features(filepath)

        self.database[key] = {
            "title": title,
            "artist": artist,
            "soundwave": soundwave,
            "frequencies": frequencies
        }
        print(f" Added '{title}' by {artist} to database.")
