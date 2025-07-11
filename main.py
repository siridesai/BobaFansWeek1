# main.py
from database.models import Song
from database.repository import save_songs_to_file, load_songs_from_file

# Create some Song objects
song1 = Song("Saturn", "SZA", "SOS Deluxe: LANA", 2024, "studio_saturn.wav")
song2 = Song("You've Got a Friend in Me", "Randy Newman", "Toy Story", 1995, "studio_youvegotafriendinme.wav")
song3 = Song("Ruthless", "The Marias", "Superclean, Vol. II", 2018, "studio_ruthless.wav")

# Create a dictionary to store the songs
# Unique ID format = artist_songName
my_songs = {
    "sza_saturn": song1,
    "randynewman_youvegotafriendinme": song2,
    "themarias_ruthless": song3
}

# Save the dictionary of songs to a file
save_songs_to_file(my_songs, "music_collection.pkl")

# Clear the current dictionary (simulate starting a new session)
my_songs = {}
print("\nMy songs dictionary after clearing:", my_songs)

# Load the songs back from the file
loaded_songs = load_songs_from_file("music_collection.pkl")

# Recording to song 
recording_to_song_key = {
    "studio_saturn.wav": "sza_saturn",
    "studio_youvegotafriendinme.wav": "randynewman_youvegotafriendinme",
    "studio_ruthless.wav": "themarias_ruthless"
} 

# Verify the loaded data
print("\nLoaded songs:")
for key, song in loaded_songs.items():
    print(f"Key: {key}")
    song.display_song_info()
    print("-" * 20)

# Access a specific song from the loaded dictionary
if "sza_saturn" in loaded_songs:
    selected_song = loaded_songs["sza_saturn"]
    print(f"\nAccessing '{selected_song.title}' from loaded data:")
    selected_song.display_song_info()
