from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    numeric_columns = [
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness"
    ]

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])

            for column in numeric_columns:
                row[column] = float(row[column])

            songs.append(row)

    print(f"Loaded songs: {len(songs)}")

    return songs



def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a weighted score and reasons for a song."""

    score = 0.0
    reasons = []

    # Genre match: +2.0 points
    # if song["genre"].lower() == user_prefs["favorite_genre"].lower():
    #     score += 2.0
    #     reasons.append("genre match (+2.0)")
    # Genre match: +1.0 point
    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 1.0
        reasons.append("genre match (+1.0)")



    # Mood match: +1.0 point
    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy similarity: up to 1.5 points
    # energy_similarity = 1 - abs(
    #     song["energy"] - user_prefs["target_energy"]
    # )
    # energy_points = 1.5 * energy_similarity
    # Energy similarity: up to 3.0 points
    energy_similarity = 1 - abs(
        song["energy"] - user_prefs["target_energy"]
    )
    energy_points = 3.0 * energy_similarity
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    # Valence similarity: up to 1.0 point
    valence_similarity = 1 - abs(
        song["valence"] - user_prefs["target_valence"]
    )
    valence_points = 1.0 * valence_similarity
    score += valence_points
    reasons.append(f"valence similarity (+{valence_points:.2f})")

    # Tempo similarity: up to 0.5 points
    tempo_similarity = max(
        0,
        1 - abs(song["tempo_bpm"] - user_prefs["target_tempo"]) / 100
    )
    tempo_points = 0.5 * tempo_similarity
    score += tempo_points
    reasons.append(f"tempo similarity (+{tempo_points:.2f})")

    # Danceability similarity: up to 0.5 points
    danceability_similarity = 1 - abs(
        song["danceability"] - user_prefs["target_danceability"]
    )
    danceability_points = 0.5 * danceability_similarity
    score += danceability_points
    reasons.append(f"danceability similarity (+{danceability_points:.2f})")

    # Acousticness similarity: up to 0.5 points
    acousticness_similarity = 1 - abs(
        song["acousticness"] - user_prefs["target_acousticness"]
    )
    acousticness_points = 0.5 * acousticness_similarity
    score += acousticness_points
    reasons.append(f"acousticness similarity (+{acousticness_points:.2f})")

    return score, reasons



def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Scores all songs and returns the top k recommendations.
    """

    scored_songs = []

    # Score every song
    for song in songs:
        score, reasons = score_song(user_prefs, song)

        # Combine the scoring reasons into one explanation
        explanation = ", ".join(reasons)

        scored_songs.append((song, score, explanation))

    # Sort songs from highest score to lowest score
    ranked_songs = sorted(
        scored_songs,
        key=lambda recommendation: recommendation[1],
        reverse=True
    )

    # Return only the top k songs
    return ranked_songs[:k]
