# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.

**MusicRec 1.0**

---

## 2. Intended Use

The proposed Music Recommener system's goal is to recommend music based on the user's preferences. It takes into account genre, mood, energy, and among other important features.

---

## 3. How the Model Works

The system using a scoring system. It gives a score to each song to see how closely it macthes to the user's preferences

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

Songs receive points for matching the user's preferred genre and mood. The system also calculates how similar each song's numerical features are to the user's targets.

Then the system sorts the songs by score and return the top 5 recommendations.

## 4. Data

The system only uses 18 songs stored in a CSV file. It contains genres such as pop, classical, hip-hop, and among other genres. Each song contains information about its genre, mood, energy, tempo, valence, danceability, and acousticness. The limitation of this dataset is that it does not contain a lot of variety and does not include every type of music.

---

## 5. Strengths

The system works excellemt whne users have clear music prefernces.
For example, Sunrise City ranked first for High-Energy Pop and Library Rain ranked first for Chill Lofi. These results matched what was expected since the songs matched the user's prefernces for the most part.

Also, the system provides reasoning for the results. For example for a recommendation we might see the following:

Storm Runner - Score: 5.52
Because: genre match (+2.0), energy similarity (+1.44), valence similarity (+0.72), tempo similarity (+0.46), danceability similarity (+0.43), acousticness similarity (+0.47)

This helps us understand why the system gave the score.

---

## 6. Limitations and Bias

- Energy Similarity now has a weight of 3.0, making it the most influential feature in the system. Although the energy-gap calculation supports both high- and low-energy preferences, it may cause songs with similar energy levels to rank highly even when their genre or mood does not match the user's preferences. In this system, also we can see that users need exact genre macthing. For example, if a user prefers pop, they will not recieve matching for indie-pop, even if related. Finally, the dataset only contains 18 songs and limits our results.

---

## 7. Evaluation

I tested the recommendation system using four different user profiles to evaluate how well it responds to different musical preferences:

- High-Energy Pop: Tests whether the system recommends energetic songs.

- Chill Lofi: Tests whether the system recommends relaxing songs

- Deep Intense Rock: Tests whether the system recommends energetic rock songs with intense moods.

- Conflicting Preferences: Tests how the system handles preferences that do not necessarily align with one another.

Overall, results show that the recommendations matched the preferecne sof each profile. For example, Sunrise City ranked first for High-Energy Pop and Library Rain ranked first for Chill Lof.

## 8. System Baseline Evaluation

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

### Weight Experiment Evaluation

```Loaded songs: 18

=======================================================
USER PROFILE: High-Energy Pop
=======================================================

Top 5 recommendations:

Sunrise City - Score: 6.87
Because: genre match (+1.0), mood match (+1.0), energy similarity (+2.61), valence similarity (+0.94), tempo similarity (+0.41), danceability similarity (+0.45), acousticness similarity (+0.46)

Gym Hero - Score: 6.26
Because: genre match (+1.0), energy similarity (+2.94), valence similarity (+0.87), tempo similarity (+0.48), danceability similarity (+0.49), acousticness similarity (+0.47)

Rooftop Lights - Score: 5.62
Because: mood match (+1.0), energy similarity (+2.43), valence similarity (+0.91), tempo similarity (+0.45), danceability similarity (+0.46), acousticness similarity (+0.38)

Funky Weekend - Score: 5.13
Because: energy similarity (+2.79), valence similarity (+0.96), tempo similarity (+0.41), danceability similarity (+0.48), acousticness similarity (+0.49)

City Bounce - Score: 4.90
Because: energy similarity (+2.73), valence similarity (+0.84), tempo similarity (+0.34), danceability similarity (+0.49), acousticness similarity (+0.49)


=======================================================
USER PROFILE: Chill Lofi
=======================================================

Top 5 recommendations:

Library Rain - Score: 7.47
Because: genre match (+1.0), mood match (+1.0), energy similarity (+3.00), valence similarity (+1.00), tempo similarity (+0.48), danceability similarity (+0.49), acousticness similarity (+0.49)

Midnight Coding - Score: 7.13
Because: genre match (+1.0), mood match (+1.0), energy similarity (+2.79), valence similarity (+0.96), tempo similarity (+0.48), danceability similarity (+0.47), acousticness similarity (+0.43)

Focus Flow - Score: 6.25
Because: genre match (+1.0), energy similarity (+2.85), valence similarity (+0.99), tempo similarity (+0.47), danceability similarity (+0.48), acousticness similarity (+0.47)

Spacewalk Thoughts - Score: 6.06
Because: mood match (+1.0), energy similarity (+2.79), valence similarity (+0.95), tempo similarity (+0.42), danceability similarity (+0.43), acousticness similarity (+0.46)

Coffee Shop Stories - Score: 5.23
Because: energy similarity (+2.94), valence similarity (+0.89), tempo similarity (+0.42), danceability similarity (+0.49), acousticness similarity (+0.48)


=======================================================
USER PROFILE: Deep Intense Rock
=======================================================

Top 5 recommendations:

Storm Runner - Score: 7.31
Because: genre match (+1.0), mood match (+1.0), energy similarity (+2.88), valence similarity (+0.97), tempo similarity (+0.48), danceability similarity (+0.47), acousticness similarity (+0.50)

Gym Hero - Score: 5.84
Because: mood match (+1.0), energy similarity (+2.94), valence similarity (+0.68), tempo similarity (+0.39), danceability similarity (+0.36), acousticness similarity (+0.47)

Iron Pulse - Score: 5.23
Because: energy similarity (+2.94), valence similarity (+0.93), tempo similarity (+0.43), danceability similarity (+0.46), acousticness similarity (+0.46)

City Bounce - Score: 4.52
Because: energy similarity (+2.73), valence similarity (+0.71), tempo similarity (+0.24), danceability similarity (+0.34), acousticness similarity (+0.49)

Night Drive Loop - Score: 4.51
Because: energy similarity (+2.40), valence similarity (+0.96), tempo similarity (+0.28), danceability similarity (+0.43), acousticness similarity (+0.44)


=======================================================
USER PROFILE: Conflicting Preferences
=======================================================

Top 5 recommendations:

Storm Runner - Score: 5.96
Because: genre match (+1.0), energy similarity (+2.88), valence similarity (+0.72), tempo similarity (+0.46), danceability similarity (+0.43), acousticness similarity (+0.47)

Iron Pulse - Score: 5.07
Because: energy similarity (+2.94), valence similarity (+0.82), tempo similarity (+0.46), danceability similarity (+0.36), acousticness similarity (+0.49)

Gym Hero - Score: 4.69
Because: energy similarity (+2.94), valence similarity (+0.43), tempo similarity (+0.36), danceability similarity (+0.46), acousticness similarity (+0.50)

City Bounce - Score: 4.34
Because: energy similarity (+2.73), valence similarity (+0.46), tempo similarity (+0.22), danceability similarity (+0.45), acousticness similarity (+0.48)

Funky Weekend - Score: 4.31
Because: energy similarity (+2.79), valence similarity (+0.34), tempo similarity (+0.28), danceability similarity (+0.43), acousticness similarity (+0.47)
```

### Evaluation Observations

- The system produced different recommendations depending on each user's musical preferences.
- Exact genre and mood matches contributed additional points to recommendation scores.
- Numerical similarities allowed songs without exact genre or mood matches to rank highly.
- The conflicting preference test demonstrated that the algorithm combines all preferences into one weighted score rather than detecting contradictions.
- After increasing the energy weight, the top-ranked song remained the same for all four profiles, but some lower-ranked songs changed positions.
- The experiment showed that energy similarity became more influential in the final ranking.

Also, for the High-Energy Pop profile, the recommendations generally matched what I expected. Sunrise City ranked first with a score of 6.56 because it matched both the preferred genre (pop) and mood (happy), while also receiving strong numerical similarity scores.

One surprising result was Gym Hero ranking second with a score of 5.79 even though it did not match the requested mood.

### Comparison Between User Profiles

**1. High-Energy Pop vs. Chill Lofi**

High-Energy Pop recommended Sunrise City, while Chill Lofi recommended Library Rain. This makes sense because one profile prefers energetic songs rather than relxaing.

**2. High-Energy Pop vs. Deep Intense Rock**

High-Energy Pop recommended Sunrise City, while Deep Intense Rock recommended Storm Runner. They both prefer energetic music, but they have different genre and mood.

**3. High-Energy Pop vs. Conflicting Preferences**

High-Energy Pop recommended Sunrise City, while Conflicting Preferences recommended Storm Runner. Their different genre preferences caused the recommendations to change.

**4. Chill Lofi vs. Deep Intense Rock**

Chill Lofi recommended Library Rain, while Deep Intense Rock recommended Storm Runner. One profile prefers calm music, while the other prefers more energtic songs

**5. Chill Lofi vs. Conflicting Preferences**

Chill Lofi recommended Library Rain, while Conflicting Preferences recommended Storm Runner.

**6. Deep Intense Rock vs. Conflicting Preferences**

Both profiles recommended Storm Runner first. However, Storm Runner scored higher for Deep Intense Rock because it matched both the preferred genre and mood.

---

## 9. Future Work

Ideas for how you would improve the model next.

- For future work, I plan to improve my dataset. I either generate more sample songs through AI, making a larger synthetic dataset, or I could actually research real-world songs to include them in the dataset. This will be more of a hybrid dataset.

- Experiment with different scoring systems by adjusting the weights of the features.

- Improve genre matching so related genres can also receive points.

---

## 10. Personal Reflection

In this project, I learned how different scoring weights on the features can affect the overall results for my system. I learned how to use AI efectively to understand the code, brainstorm improvements, and identify possible problems in the coding logic. I was suprised that slight adjustments to the scoring system can affect the results. If I were to continue on the project I would improve the scoring system, add more songs to the dataset, and even add website for this system.
