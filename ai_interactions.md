# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**Prompts used:**

<!-- Paste the key prompts you gave the agent -->

- I want to expand my existing music recommender dataset by adding at least five advanced song attributes that are not currently included. My dataset contains 18 fictional songs. Suggest five useful attributes that could improve recommendations while preserving all existing song information

- Help me add the following attributes to my existing songs.csv dataset: popularity (0–100), release decade, detailed mood tags, language, and explicit content status. Keep all existing songs and their original feature values unchanged.

- Update my recommender.py and main.py based on the newly updated csv file

- I am developing a Python music recommendation system. I want to add multiple scoring modes, including Genre-First, Mood-First, and Energy-Focused.

Please review my attached recommender.py file and help me brainstorm a design pattern that would keep the code modular.

I am considering the Strategy design pattern.

Please explain:

1. How the Strategy pattern would work in my existing recommender.
2. How I could organize the different scoring algorithms.
3. How main.py could allow users to select a scoring mode.
4. How this design avoids duplicating code and makes the project easier to maintain.

Please focus on the design and explanation first. Do not rewrite my entire code yet.

- Update my code with the discussed chnages.

- I am developing a Python music recommendation system. I have attached my current recommender.py file.

- I want to implement a Diversity Penalty feature that prevents the recommendation system from suggesting too many songs from the same artist or genre in the top recommendations.

- Asked AI to improve the readability of your terminal output by providing a formatted table or summary.

**What did the agent generate or change?**

<!-- List the files edited, code generated, or commands run -->

For expanding dataset the output was:
We'll preserve all your existing data and add five new columns:

1. popularity — score from 0–100.
2. release_decade — decade the song was released.
3. mood_tags — additional descriptive tags.
4. language — song language.
5. explicit — whether the song contains explicit content.

Done! I expanded your CSV with 5 additional attributes, keeping all 18 original songs and their existing data unchanged. Then AI provided me with the updated CSV

FOR CODE ABOUT RECOMMENDER.PY and MAIN.PY:
Updated code was given as well as main.py suggestions

```python
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field
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

    # Advanced preferences (optional)
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
    Required by src/main.py
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

            # Convert explicit into a Boolean
            row["explicit"] = row["explicit"].strip().lower() == "true"

            songs.append(row)

    print(f"Loaded songs: {len(songs)}")

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a weighted score and reasons for a song."""

    score = 0.0
    reasons = []

    # Genre match: +2.0 points
    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match: +1.0 point
    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy similarity: up to 1.5 points
    energy_similarity = max(
        0,
        1 - abs(song["energy"] - user_prefs["target_energy"])
    )
    energy_points = 1.5 * energy_similarity
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    # Valence similarity: up to 1.0 point
    valence_similarity = max(
        0,
        1 - abs(song["valence"] - user_prefs["target_valence"])
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
    danceability_similarity = max(
        0,
        1 - abs(song["danceability"] - user_prefs["target_danceability"])
    )
    danceability_points = 0.5 * danceability_similarity
    score += danceability_points
    reasons.append(f"danceability similarity (+{danceability_points:.2f})")

    # Acousticness similarity: up to 0.5 points
    acousticness_similarity = max(
        0,
        1 - abs(song["acousticness"] - user_prefs["target_acousticness"])
    )
    acousticness_points = 0.5 * acousticness_similarity
    score += acousticness_points
    reasons.append(f"acousticness similarity (+{acousticness_points:.2f})")

    # ---------------------------------------
    # ADVANCED SONG FEATURES
    # ---------------------------------------

    # Popularity similarity: up to 0.5 points
    if user_prefs.get("target_popularity") is not None:
        popularity_similarity = max(
            0,
            1 - abs(
                song["popularity"] - user_prefs["target_popularity"]
            ) / 100
        )
        popularity_points = 0.5 * popularity_similarity
        score += popularity_points
        reasons.append(
            f"popularity similarity (+{popularity_points:.2f})"
        )

    # Release decade match: up to 0.5 points
    if user_prefs.get("preferred_decade") is not None:
        if song["release_decade"] == user_prefs["preferred_decade"]:
            score += 0.5
            reasons.append("release decade match (+0.50)")

    # Detailed mood tags: up to 0.5 points
    preferred_tags = user_prefs.get("preferred_mood_tags", [])

    if preferred_tags:
        song_tags = song["mood_tags"]

        matching_tags = [
            tag for tag in preferred_tags
            if tag.lower() in song_tags
        ]

        tag_similarity = len(matching_tags) / len(preferred_tags)
        tag_points = 0.5 * tag_similarity

        score += tag_points

        if matching_tags:
            reasons.append(
                f"mood tags match (+{tag_points:.2f})"
            )

    # Language match: up to 0.5 points
    preferred_language = user_prefs.get("preferred_language")

    if preferred_language is not None:
        if song["language"].lower() == preferred_language.lower():
            score += 0.5
            reasons.append("language match (+0.50)")

    # Explicit content preference: up to 0.5 points
    prefer_explicit = user_prefs.get("prefer_explicit")

    if prefer_explicit is not None:
        if song["explicit"] == prefer_explicit:
            score += 0.5
            reasons.append("explicit preference match (+0.50)")

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Scores all songs and returns the top k recommendations.
    """

    scored_songs = []

    # Score every song
    for song in songs:
        score, reasons = score_song(user_prefs, song)

        # Combine scoring reasons into one explanation
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


# Paste the rest of your updated recommender.py code here
```

for challenge 3 it gave me what code to chnage

```python

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    strategy: str = "Genre-First"
) -> List[Tuple[Dict, float, str]]:
    """
    Scores songs using the selected strategy and applies
    diversity penalties to avoid too many repeated artists
    and genres in the recommendations.
    """

    scored_songs = []

    # Score every song using the selected strategy
    for song in songs:
        score, reasons = score_song(user_prefs, song, strategy)

        explanation = ", ".join(reasons)

        scored_songs.append((song, score, explanation))

    recommendations = []

    # Track artists and genres already recommended
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

        # Evaluate every remaining song
        for i, (song, original_score, explanation) in enumerate(scored_songs):

            adjusted_score = original_score
            diversity_reasons = []

            artist = song["artist"].strip().lower()
            genre = song["genre"].strip().lower()

            # Penalize repeated artists
            artist_count = selected_artists.get(artist, 0)

            if artist_count > 0:
                penalty = artist_penalty * artist_count
                adjusted_score -= penalty

                diversity_reasons.append(
                    f"repeated artist (-{penalty:.2f})"
                )

            # Penalize repeated genres
            genre_count = selected_genres.get(genre, 0)

            if genre_count > 0:
                penalty = genre_penalty * genre_count
                adjusted_score -= penalty

                diversity_reasons.append(
                    f"repeated genre (-{penalty:.2f})"
                )

            # Keep track of the highest adjusted score
            if adjusted_score > best_adjusted_score:
                best_adjusted_score = adjusted_score
                best_index = i

                best_explanation = explanation

                if diversity_reasons:
                    best_explanation += ", " + ", ".join(diversity_reasons)

        # Select the best remaining song
        best_song = scored_songs.pop(best_index)[0]

        recommendations.append(
            (best_song, best_adjusted_score, best_explanation)
        )

        # Update artist and genre counts
        artist = best_song["artist"].strip().lower()
        genre = best_song["genre"].strip().lower()

        selected_artists[artist] = selected_artists.get(artist, 0) + 1
        selected_genres[genre] = selected_genres.get(genre, 0) + 1

    return recommendations

```

For visual summary table the AI gave me updated main.py and recommdner.py to have visual table.

**What did you verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

For manually verifying the CSV file I just downloaded and looked over all the features for each song. Wanted to see if all songs seemed consistent. For code, I manually tested through the terminal and it was succesful.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

I used a Strategy-inspired design pattern. The implementation uses a dictionary called SCORING_STRATEGIES to define different scoring configurations: Genre-First, Mood-First, and Energy-Focused.

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

It suggested using the Strategy design pattern so that different scoring approaches could be organized separately without duplicating the recommendation logic. It helped me implemnet these in code and I manually reviewed them. I also needed to add changes to main.py to pick what mode we want.

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->

The pattern appears in recommender.py through the the score_song() function. We see it added the new features that need to be taken into account. We can also see chnages in the main.py to pic which mode we want
