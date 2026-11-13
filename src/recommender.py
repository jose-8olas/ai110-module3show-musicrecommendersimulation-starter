
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
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

    # Advanced song features
    popularity: float = 50.0
    release_decade: int = 2020
    mood_tags: List[str] = field(default_factory=list)
    language: str = "English"
    explicit: bool = False


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

    # Advanced preferences
    target_popularity: Optional[float] = None
    preferred_decade: Optional[int] = None
    preferred_mood_tags: List[str] = field(default_factory=list)
    preferred_language: Optional[str] = None
    prefer_explicit: Optional[bool] = None


class Recommender:
    """
    OOP implementation of the recommendation logic.
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
    """

    songs = []

    numeric_columns = [
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
        "popularity"
    ]

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])

            for column in numeric_columns:
                row[column] = float(row[column])

            row["release_decade"] = int(row["release_decade"])

            # Convert mood tags into a list
            row["mood_tags"] = [
                tag.strip().lower()
                for tag in row["mood_tags"].split("|")
                if tag.strip()
            ]

            # Convert explicit into Boolean
            row["explicit"] = (
                row["explicit"].strip().lower() == "true"
            )

            songs.append(row)

    print(f"Loaded songs: {len(songs)}")

    return songs


# =======================================
# CHALLENGE 2: SCORING STRATEGIES
# =======================================

SCORING_STRATEGIES = {

    "Genre-First": {
        "genre": 4.0,
        "mood": 1.0,
        "energy": 1.0,
        "valence": 0.5,
        "tempo": 0.25,
        "danceability": 0.25,
        "acousticness": 0.25
    },

    "Mood-First": {
        "genre": 1.0,
        "mood": 3.0,
        "energy": 1.0,
        "valence": 1.0,
        "tempo": 0.25,
        "danceability": 0.25,
        "acousticness": 0.25
    },

    "Energy-Focused": {
        "genre": 1.0,
        "mood": 0.5,
        "energy": 3.0,
        "valence": 0.5,
        "tempo": 1.0,
        "danceability": 1.0,
        "acousticness": 0.25
    }
}


def score_song(
    user_prefs: Dict,
    song: Dict,
    strategy: str = "Genre-First"
) -> Tuple[float, List[str]]:
    """
    Calculates a song score using the selected scoring strategy.
    """

    if strategy not in SCORING_STRATEGIES:
        raise ValueError(
            f"Unknown scoring strategy: {strategy}. "
            f"Available strategies: {list(SCORING_STRATEGIES.keys())}"
        )

    weights = SCORING_STRATEGIES[strategy]

    score = 0.0
    reasons = []

    # ---------------------------------------
    # GENRE MATCH
    # ---------------------------------------

    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        points = weights["genre"]
        score += points
        reasons.append(f"genre match (+{points:.2f})")

    # ---------------------------------------
    # MOOD MATCH
    # ---------------------------------------

    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        points = weights["mood"]
        score += points
        reasons.append(f"mood match (+{points:.2f})")

    # ---------------------------------------
    # ENERGY SIMILARITY
    # ---------------------------------------

    energy_similarity = max(
        0,
        1 - abs(song["energy"] - user_prefs["target_energy"])
    )

    points = weights["energy"] * energy_similarity
    score += points
    reasons.append(f"energy similarity (+{points:.2f})")

    # ---------------------------------------
    # VALENCE SIMILARITY
    # ---------------------------------------

    valence_similarity = max(
        0,
        1 - abs(song["valence"] - user_prefs["target_valence"])
    )

    points = weights["valence"] * valence_similarity
    score += points
    reasons.append(f"valence similarity (+{points:.2f})")

    # ---------------------------------------
    # TEMPO SIMILARITY
    # ---------------------------------------

    tempo_similarity = max(
        0,
        1 - abs(song["tempo_bpm"] - user_prefs["target_tempo"]) / 100
    )

    points = weights["tempo"] * tempo_similarity
    score += points
    reasons.append(f"tempo similarity (+{points:.2f})")

    # ---------------------------------------
    # DANCEABILITY SIMILARITY
    # ---------------------------------------

    danceability_similarity = max(
        0,
        1 - abs(
            song["danceability"] - user_prefs["target_danceability"]
        )
    )

    points = weights["danceability"] * danceability_similarity
    score += points
    reasons.append(f"danceability similarity (+{points:.2f})")

    # ---------------------------------------
    # ACOUSTICNESS SIMILARITY
    # ---------------------------------------

    acousticness_similarity = max(
        0,
        1 - abs(
            song["acousticness"] - user_prefs["target_acousticness"]
        )
    )

    points = weights["acousticness"] * acousticness_similarity
    score += points
    reasons.append(f"acousticness similarity (+{points:.2f})")

    # =======================================
    # CHALLENGE 1: ADVANCED SONG FEATURES
    # =======================================

    # Popularity similarity
    if user_prefs.get("target_popularity") is not None:

        popularity_similarity = max(
            0,
            1 - abs(
                song["popularity"] - user_prefs["target_popularity"]
            ) / 100
        )

        points = 0.5 * popularity_similarity
        score += points

        reasons.append(
            f"popularity similarity (+{points:.2f})"
        )

    # Release decade match
    if user_prefs.get("preferred_decade") is not None:

        if song["release_decade"] == user_prefs["preferred_decade"]:
            score += 0.5
            reasons.append("release decade match (+0.50)")

    # Detailed mood tags
    preferred_tags = user_prefs.get("preferred_mood_tags", [])

    if preferred_tags:

        song_tags = song["mood_tags"]

        matching_tags = [
            tag for tag in preferred_tags
            if tag.lower() in song_tags
        ]

        tag_similarity = len(matching_tags) / len(preferred_tags)

        points = 0.5 * tag_similarity
        score += points

        if matching_tags:
            reasons.append(
                f"mood tags match (+{points:.2f})"
            )

    # Language match
    preferred_language = user_prefs.get("preferred_language")

    if preferred_language is not None:

        if song["language"].lower() == preferred_language.lower():
            score += 0.5
            reasons.append("language match (+0.50)")

    # Explicit content preference
    prefer_explicit = user_prefs.get("prefer_explicit")

    if prefer_explicit is not None:

        if song["explicit"] == prefer_explicit:
            score += 0.5
            reasons.append("explicit preference match (+0.50)")

    return score, reasons


# =======================================
# CHALLENGE 3: DIVERSITY PENALTY
# =======================================

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    strategy: str = "Genre-First"
) -> List[Tuple[Dict, float, str]]:
    """
    Scores songs using the selected strategy and applies
    diversity penalties to repeated artists and genres.
    """

    scored_songs = []

    # Calculate original scores for all songs
    for song in songs:

        score, reasons = score_song(
            user_prefs,
            song,
            strategy
        )

        explanation = ", ".join(reasons)

        scored_songs.append(
            (song, score, explanation)
        )

    recommendations = []

    # Track previously selected artists and genres
    selected_artists = {}
    selected_genres = {}

    # Diversity penalty values
    artist_penalty = 2.0
    genre_penalty = 0.75

    # Select songs one at a time
    while scored_songs and len(recommendations) < k:

        best_index = -1
        best_adjusted_score = float("-inf")
        best_explanation = ""

        # Evaluate remaining songs
        for i, (song, original_score, explanation) in enumerate(scored_songs):

            adjusted_score = original_score
            diversity_reasons = []

            artist = song["artist"].strip().lower()
            genre = song["genre"].strip().lower()

            # Artist diversity penalty
            artist_count = selected_artists.get(artist, 0)

            if artist_count > 0:

                penalty = artist_penalty * artist_count
                adjusted_score -= penalty

                diversity_reasons.append(
                    f"repeated artist (-{penalty:.2f})"
                )

            # Genre diversity penalty
            genre_count = selected_genres.get(genre, 0)

            if genre_count > 0:

                penalty = genre_penalty * genre_count
                adjusted_score -= penalty

                diversity_reasons.append(
                    f"repeated genre (-{penalty:.2f})"
                )

            # Find the highest adjusted score
            if adjusted_score > best_adjusted_score:

                best_adjusted_score = adjusted_score
                best_index = i
                best_explanation = explanation

                if diversity_reasons:

                    best_explanation += ", " + ", ".join(
                        diversity_reasons
                    )

        # Select the best song
        best_song = scored_songs.pop(best_index)[0]

        recommendations.append(
            (
                best_song,
                best_adjusted_score,
                best_explanation
            )
        )

        # Update artist and genre counts
        artist = best_song["artist"].strip().lower()
        genre = best_song["genre"].strip().lower()

        selected_artists[artist] = (
            selected_artists.get(artist, 0) + 1
        )

        selected_genres[genre] = (
            selected_genres.get(genre, 0) + 1
        )

    return recommendations
