"""Shared helpers for loading the FMA music data with readable column names."""
from pathlib import Path

import pandas as pd

AUDIO = ["acousticness", "danceability", "energy", "instrumentalness",
         "liveness", "speechiness", "tempo", "valence"]
SOCIAL = ["artist_discovery", "artist_familiarity", "artist_hotttnesss",
          "song_currency", "song_hotttnesss"]
TEMPORAL = [f"temporal_{i:03d}" for i in range(1, 225)]
FEATURES = AUDIO + SOCIAL + TEMPORAL
COLUMNS = ["genre"] + FEATURES

RAW_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "music.csv"


def load_music(path: Path = RAW_PATH) -> pd.DataFrame:
    """Load music.csv (no header row) and attach the FMA Echonest column names."""
    music = pd.read_csv(path, header=None, names=COLUMNS)
    music["genre"] = music["genre"].str.strip()  # some labels have leading spaces
    return music
