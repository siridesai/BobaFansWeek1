import pickle
from .models import Song # Relative import of the Song class

def save_songs_to_file(songs_dict, filename="songs_data.pkl"):
    """
    Saves a dictionary of Song objects to a file using pickle.

    Args:
        songs_dict (dict): A dictionary where keys are song identifiers
                           and values are Song objects.
        filename (str): The name of the file to save to. Defaults to "songs_data.pkl".
    """
    try:
        with open(filename, "wb") as f:
            pickle.dump(songs_dict, f)
        print(f"Song data saved to {filename}")
    except Exception as e:
        print(f"Error saving song data: {e}")

def load_songs_from_file(filename="songs_data.pkl"):
    """
    Loads a dictionary of Song objects from a file using pickle.

    Args:
        filename (str): The name of the file to load from. Defaults to "songs_data.pkl".

    Returns:
        dict: A dictionary of Song objects, or an empty dictionary if the file
              doesn't exist or an error occurs.
    """
    try:
        with open(filename, "rb") as f:
            songs_dict = pickle.load(f)
        print(f"Song data loaded from {filename}")
        return songs_dict
    except FileNotFoundError:
        print(f"File '{filename}' not found. Returning an empty dictionary.")
        return {}
    except Exception as e:
        print(f"Error loading song data: {e}")
        return {}
