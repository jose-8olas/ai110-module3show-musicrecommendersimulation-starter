# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Real-world applications like Spotify, use recommednation systmes to help recommend songs to users. For example, if people have similar taste and they liked a specific song then the system will probably suggest that song to the other person with similar taste. Also, these applications might also analyze your most listened songs and liked songs.
Meanwhile other systems may use content-based filering as well. The system might recommend similar sings based on the song's genre, mood, or other features.

The music recommendation for the project will use content-based filtering based on the user's prefernces of music. So, this system will compare songs with the user perferred songs to decide what music songs to recommend.

Songs have several features:

- Title
- Genre
- Artist name
- Mood
- Tempo
- Acousticness
- Danceability
- Energy
- Valence

For the system, the User Profile will store the user's prefernces. These include:

- Preferred genre
- Preferred mood
- Preferred energy level
- Preferred tempo
- Preferred valence
- Preferred danceability
- Whether they like acoustic music

The Recommender compares each song's features against the user's preferences.

For example:

- Matching the preferred genre earns more points.
- Matching the preferred mood earns more points.
- Energy, valence, and other numerical features receive higher scores when they are closer to the user's preferred values.

After calculating the scores, the system will rank from highest to the lowest and retrieve the top 5 songs with the highest scores.

### Algorithm Recipe

The recommender uses a weighted scoring system with a maximum possible score of 7.0 points.

| Feature      | Scoring Rule                                               | Maximum Points |
| ------------ | ---------------------------------------------------------- | -------------: |
| Genre        | +2.0 if the song's genre matches the user's favorite genre |            2.0 |
| Mood         | +1.0 if the song's mood matches the user's favorite mood   |            1.0 |
| Energy       | 1.5 × (1 - absolute difference)                            |            1.5 |
| Valence      | 1.0 × (1 - absolute difference)                            |            1.0 |
| Tempo        | 0.5 × max(0, 1 - absolute difference / 100)                |            0.5 |
| Danceability | 0.5 × (1 - absolute difference)                            |            0.5 |
| Acousticness | 0.5 × (1 - absolute difference)                            |            0.5 |
| **Total**    |                                                            |        **7.0** |

For numerical features between 0 and 1, similarity is calculated using:

`Similarity = 1 - abs(song_value - target_value)`

For tempo, the difference is divided by 100 BPM, and the similarity cannot fall below zero.

### Potential Biases and Limitations

The recommendation system has several potential biases and limitations:

- **Genre Prioritization:** Genre receives 2.0 points. The most points out of all. This means genre will be prioritized more than other fetaures
- **Limited Dataset:** The dataset contains only 18 songs, so recommendations are limited.
- **Matching:** Genre and moods require exact matches. For example, "indie pop" and "pop" are treated differently.
- **Diversity:** Not much variety of artists and some recommendations may coem from same artist or genre.

The following flowchart illustrates how the Music Recommender processes user preferences and ranks songs from the CSV dataset.

```mermaid
flowchart TD
    A["Input: User Preferences"]
    B["Load songs.csv"]
    C["Loop Through Each Song"]
    D["Compare Song Features with User Preferences"]
    E["Calculate Weighted Score (Maximum 7 Points)"]
    F["Store Song, Score, and Explanation"]
    G{"More Songs?"}
    H["Sort Songs by Score (Highest to Lowest)"]
    I["Output: Top 5 Recommendations"]

    A --> C
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G -->|Yes| C
    G -->|No| H
    H --> I
```

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 18

Top recommendations:

Sunrise City - Score: 6.91
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.47), valence similarity (+0.96), tempo similarity (+0.49), danceability similarity (+0.49), acousticness similarity (+0.49)

Gym Hero - Score: 5.60
Because: genre match (+2.0), energy similarity (+1.30), valence similarity (+0.97), tempo similarity (+0.44), danceability similarity (+0.46), acousticness similarity (+0.42)

Rooftop Lights - Score: 4.82
Because: mood match (+1.0), energy similarity (+1.44), valence similarity (+0.99), tempo similarity (+0.48), danceability similarity (+0.49), acousticness similarity (+0.43)

Funky Weekend - Score: 3.69
Because: energy similarity (+1.38), valence similarity (+0.94), tempo similarity (+0.48), danceability similarity (+0.43), acousticness similarity (+0.46)

City Bounce - Score: 3.65
Because: energy similarity (+1.41), valence similarity (+0.94), tempo similarity (+0.42), danceability similarity (+0.45), acousticness similarity (+0.44)
```

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

## System Evaluation

The recommender was evaluated using four different user preference profiles to observe how the scoring algorithm behaves under different listening preferences.

### 1. High-Energy Pop

```Loaded songs: 18

=======================================================
USER PROFILE: High-Energy Pop
=======================================================

Top 5 recommendations:

Sunrise City - Score: 6.56
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.30), valence similarity (+0.94), tempo similarity (+0.41), danceability similarity (+0.45), acousticness similarity (+0.46)

Gym Hero - Score: 5.79
Because: genre match (+2.0), energy similarity (+1.47), valence similarity (+0.87), tempo similarity (+0.48), danceability similarity (+0.49), acousticness similarity (+0.47)

Rooftop Lights - Score: 4.40
Because: mood match (+1.0), energy similarity (+1.22), valence similarity (+0.91), tempo similarity (+0.45), danceability similarity (+0.46), acousticness similarity (+0.38)

Funky Weekend - Score: 3.73
Because: energy similarity (+1.40), valence similarity (+0.96), tempo similarity (+0.41), danceability similarity (+0.48), acousticness similarity (+0.49)

City Bounce - Score: 3.54
Because: energy similarity (+1.36), valence similarity (+0.84), tempo similarity (+0.34), danceability similarity (+0.49), acousticness similarity (+0.49)
```

### 2. Chill Lofi

```=======================================================
USER PROFILE: Chill Lofi
=======================================================

Top 5 recommendations:

Library Rain - Score: 6.97
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.50), valence similarity (+1.00), tempo similarity (+0.48), danceability similarity (+0.49), acousticness similarity (+0.49)

Midnight Coding - Score: 6.73
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.40), valence similarity (+0.96), tempo similarity (+0.48), danceability similarity (+0.47), acousticness similarity (+0.43)

Focus Flow - Score: 5.83
Because: genre match (+2.0), energy similarity (+1.42), valence similarity (+0.99), tempo similarity (+0.47), danceability similarity (+0.48), acousticness similarity (+0.47)

Spacewalk Thoughts - Score: 4.66
Because: mood match (+1.0), energy similarity (+1.40), valence similarity (+0.95), tempo similarity (+0.42), danceability similarity (+0.43), acousticness similarity (+0.46)

Coffee Shop Stories - Score: 3.76
Because: energy similarity (+1.47), valence similarity (+0.89), tempo similarity (+0.42), danceability similarity (+0.49), acousticness similarity (+0.48)
```

### 3. Deep Intense Rock

```=======================================================
USER PROFILE: Deep Intense Rock
=======================================================

Top 5 recommendations:

Storm Runner - Score: 6.87
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.44), valence similarity (+0.97), tempo similarity (+0.48), danceability similarity (+0.47), acousticness similarity (+0.50)

Gym Hero - Score: 4.37
Because: mood match (+1.0), energy similarity (+1.47), valence similarity (+0.68), tempo similarity (+0.39), danceability similarity (+0.36), acousticness similarity (+0.47)

Iron Pulse - Score: 3.76
Because: energy similarity (+1.47), valence similarity (+0.93), tempo similarity (+0.43), danceability similarity (+0.46), acousticness similarity (+0.46)

Night Drive Loop - Score: 3.31
Because: energy similarity (+1.20), valence similarity (+0.96), tempo similarity (+0.28), danceability similarity (+0.43), acousticness similarity (+0.44)

City Bounce - Score: 3.16
Because: energy similarity (+1.36), valence similarity (+0.71), tempo similarity (+0.24), danceability similarity (+0.34), acousticness similarity (+0.49)
```

### 4. Conflicting Preferences (Adversarial Test)

```=======================================================
USER PROFILE: Conflicting Preferences
=======================================================

Top 5 recommendations:

Storm Runner - Score: 5.52
Because: genre match (+2.0), energy similarity (+1.44), valence similarity (+0.72), tempo similarity (+0.46), danceability similarity (+0.43), acousticness similarity (+0.47)

Iron Pulse - Score: 3.60
Because: energy similarity (+1.47), valence similarity (+0.82), tempo similarity (+0.46), danceability similarity (+0.36), acousticness similarity (+0.49)

Gym Hero - Score: 3.22
Because: energy similarity (+1.47), valence similarity (+0.43), tempo similarity (+0.36), danceability similarity (+0.46), acousticness similarity (+0.50)

Night Drive Loop - Score: 3.04
Because: energy similarity (+1.20), valence similarity (+0.71), tempo similarity (+0.25), danceability similarity (+0.46), acousticness similarity (+0.42)

City Bounce - Score: 2.97
Because: energy similarity (+1.36), valence similarity (+0.46), tempo similarity (+0.22), danceability similarity (+0.45), acousticness similarity (+0.48)
```

### Evaluation Observations

- The system successfully ranked songs according to different user preferences.
- Exact genre and mood matches contributed additional points to recommendation scores.
- Numerical similarities allowed songs without exact genre or mood matches to rank highly.
- The conflicting preference test demonstrated that the algorithm combines all preferences into one weighted score rather than detecting contradictions.

Also, for the High-Energy Pop profile, the recommendations generally matched what I expected. Sunrise City ranked first with a score of 6.56 because it matched both the preferred genre (pop) and mood (happy), while also receiving strong numerical similarity scores.

One surprising result was Gym Hero ranking second with a score of 5.79 even though it did not match the requested mood.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
