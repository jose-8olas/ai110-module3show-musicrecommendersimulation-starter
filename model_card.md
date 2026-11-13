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

## 8. Future Work

Ideas for how you would improve the model next.

- For future work, I plan to improve my dataset. I either generate more sample songs through AI, making a larger synthetic dataset, or I could actually research real-world songs to include them in the dataset. This will be more of a hybrid dataset.

- Experiment with different scoring systems by adjusting the weights of the features.

- Improve genre matching so related genres can also receive points.

---

## 9. Personal Reflection

In this project, I learned how different scoring weights on the features can affect the overall results for my system. I learned how to use AI efectively to understand the code, brainstorm improvements, and identify possible problems in the coding logic. I was suprised that slight adjustments to the scoring system can affect the results. If I were to continue on the project I would improve the scoring system, add more songs to the dataset, and even add website for this system.
