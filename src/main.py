
"""
Command line runner for the Music Recommender Simulation.

This file loads the song dataset and evaluates recommendations
using multiple user preference profiles.
"""

from pathlib import Path
from src.recommender import load_songs, recommend_songs


def main() -> None:
    # Locate the project root and CSV dataset
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "songs.csv"

    songs = load_songs(str(csv_path))

    # Define multiple user preference profiles
    user_profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.95,
            "target_tempo": 135,
            "target_valence": 0.90,
            "target_danceability": 0.90,
            "target_acousticness": 0.10
        },

        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.35,
            "target_tempo": 75,
            "target_valence": 0.60,
            "target_danceability": 0.55,
            "target_acousticness": 0.85
        },

        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "target_tempo": 155,
            "target_valence": 0.45,
            "target_danceability": 0.60,
            "target_acousticness": 0.10
        },

        # Adversarial profile: conflicting mood and energy preferences
        "Conflicting Preferences": {
            "favorite_genre": "rock",
            "favorite_mood": "sad",
            "target_energy": 0.95,
            "target_tempo": 160,
            "target_valence": 0.20,
            "target_danceability": 0.80,
            "target_acousticness": 0.05
        }
    }

    # Generate recommendations for each profile
    for profile_name, user_prefs in user_profiles.items():

        print("\n" + "=" * 55)
        print(f"USER PROFILE: {profile_name}")
        print("=" * 55)

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\nTop 5 recommendations:\n")

        for rec in recommendations:
            song, score, explanation = rec

            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
