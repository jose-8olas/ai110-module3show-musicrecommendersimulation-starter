
from pathlib import Path
import textwrap

from src.recommender import load_songs, recommend_songs


# =======================================
# CHALLENGE 4: FORMATTED TERMINAL OUTPUT
# =======================================

def print_recommendations_table(recommendations):
    """
    Displays recommendations in a formatted ASCII table.
    Long explanations are wrapped across multiple lines.
    """

    headers = [
        "Rank",
        "Song Title",
        "Artist",
        "Genre",
        "Score",
        "Reasons"
    ]

    # Maximum width of each column
    widths = [4, 22, 18, 12, 7, 55]

    def format_row(values):

        wrapped_values = []

        # Wrap the content of each column
        for i, value in enumerate(values):

            wrapped = textwrap.wrap(
                str(value),
                width=widths[i],
                break_long_words=True,
                break_on_hyphens=False
            )

            wrapped_values.append(
                wrapped if wrapped else [""]
            )

        # Determine the number of lines needed
        max_lines = max(
            len(column) for column in wrapped_values
        )

        # Print each line
        for line in range(max_lines):

            formatted_cells = []

            for i, column in enumerate(wrapped_values):

                if line < len(column):
                    cell = column[line]
                else:
                    cell = ""

                formatted_cells.append(
                    cell.ljust(widths[i])
                )

            print("| " + " | ".join(formatted_cells) + " |")

    # Create table border
    border = "+-" + "-+-".join(
        "-" * width for width in widths
    ) + "-+"

    # Handle empty recommendations
    if not recommendations:
        print("No recommendations available.")
        return

    print(border)

    # Print table headers
    format_row(headers)

    print(border)

    # Print recommendation rows
    for rank, (song, score, reasons) in enumerate(
        recommendations,
        start=1
    ):

        row = [
            rank,
            song["title"],
            song["artist"],
            song["genre"],
            f"{score:.2f}",
            reasons
        ]

        format_row(row)

        # Separate recommendations
        print(border)


# =======================================
# MAIN PROGRAM
# =======================================

def main() -> None:

    # ---------------------------------------
    # LOAD SONG DATA
    # ---------------------------------------

    project_root = Path(__file__).resolve().parent.parent

    csv_path = project_root / "data" / "songs.csv"

    songs = load_songs(str(csv_path))

    # ---------------------------------------
    # USER PROFILES
    # ---------------------------------------

    user_profiles = {

        "High-Energy Pop": {
            "favorite_genre": "Pop",
            "favorite_mood": "Happy",
            "target_energy": 0.9,
            "target_valence": 0.8,
            "target_tempo": 120,
            "target_danceability": 0.9,
            "target_acousticness": 0.1,
            "likes_acoustic": False,
            "target_popularity": 85,
            "preferred_decade": 2020,
            "preferred_mood_tags": ["happy", "energetic"],
            "preferred_language": "English",
            "prefer_explicit": False
        },

        "Chill Lofi": {
            "favorite_genre": "Lo-fi",
            "favorite_mood": "Calm",
            "target_energy": 0.3,
            "target_valence": 0.5,
            "target_tempo": 80,
            "target_danceability": 0.4,
            "target_acousticness": 0.8,
            "likes_acoustic": True,
            "target_popularity": 40,
            "preferred_decade": 2020,
            "preferred_mood_tags": ["calm", "relaxed"],
            "preferred_language": "Instrumental",
            "prefer_explicit": False
        },

        "Deep Intense Rock": {
            "favorite_genre": "Rock",
            "favorite_mood": "Intense",
            "target_energy": 0.9,
            "target_valence": 0.3,
            "target_tempo": 140,
            "target_danceability": 0.6,
            "target_acousticness": 0.2,
            "likes_acoustic": False,
            "target_popularity": 70,
            "preferred_decade": 2010,
            "preferred_mood_tags": ["intense", "dark"],
            "preferred_language": "English",
            "prefer_explicit": True
        },

        "Conflicting Preferences": {
            "favorite_genre": "Classical",
            "favorite_mood": "Happy",
            "target_energy": 0.2,
            "target_valence": 0.9,
            "target_tempo": 180,
            "target_danceability": 0.9,
            "target_acousticness": 0.9,
            "likes_acoustic": True,
            "target_popularity": 95,
            "preferred_decade": 2010,
            "preferred_mood_tags": ["happy", "energetic"],
            "preferred_language": "English",
            "prefer_explicit": False
        }
    }

    # ---------------------------------------
    # CHALLENGE 2: STRATEGY SELECTION
    # ---------------------------------------

    scoring_modes = {
        "1": "Genre-First",
        "2": "Mood-First",
        "3": "Energy-Focused"
    }

    print("\n======================================")
    print("       MUSIC RECOMMENDATION SYSTEM")
    print("======================================")

    print("\nSelect a recommendation strategy:\n")

    for number, strategy in scoring_modes.items():
        print(f"  {number}. {strategy}")

    # Get user's strategy selection
    while True:

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice in scoring_modes:
            selected_strategy = scoring_modes[choice]
            break

        print("Invalid choice. Please enter 1, 2, or 3.")

    print("\nSelected strategy:", selected_strategy)

    # ---------------------------------------
    # GENERATE RECOMMENDATIONS
    # ---------------------------------------

    for profile_name, user_prefs in user_profiles.items():

        print("\n")
        print("=" * 75)
        print(f"USER PROFILE: {profile_name}")
        print(f"STRATEGY: {selected_strategy}")
        print("=" * 75)

        recommendations = recommend_songs(
            user_prefs,
            songs,
            k=5,
            strategy=selected_strategy
        )

        print_recommendations_table(recommendations)


if __name__ == "__main__":
    main()
