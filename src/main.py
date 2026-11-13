
"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from pathlib import Path
from src.recommender import load_songs, recommend_songs


def main() -> None:
    # Locate the project root and CSV dataset
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "songs.csv"

    songs = load_songs(str(csv_path))

    # User's musical preferences
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_tempo": 120,
        "target_valence": 0.80,
        "target_danceability": 0.80,
        "target_acousticness": 0.20
    }

    # Generate the top 5 recommendations
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")

    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
