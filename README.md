# BigDataProject-ITCS6100

# Team

## Members:
- Ramya Jampani
- Chetan Subhash Chunduru
- Himanshi Khatri
- Revanth Kumar Galla
- Satya Sai Rajesh Parvatareddy

## Communication plan to include project artifact repository:
We will establish a communication plan that includes using a project artifact repository, such as GitHub, for version control and collaboration on code and project documentation. We will also use a meeting platform, such as Google Meet or Zoom, for team meetings, and take meeting notes for reference.

Git link: [https://github.com/hkholic13/BigDataProject-ITCS6100](https://github.com/hkholic13/BigDataProject-ITCS6100)

## First Choice :

# Selection of data to analyze

We will carefully select the domain and data for our project, which in this case, will be the "H&M Personalized Fashion Recommendations" dataset provided by the competition organizers. We will analyze the dataset and understand its structure, features, and potential use cases for fashion recommendation.

Kaggle Link: [https://www.kaggle.com/code/bearcater/h-m-personalized-fashion-recommendations](https://www.kaggle.com/code/bearcater/h-m-personalized-fashion-recommendations)

## Files:
- images/ - a folder of images corresponding to each article_id; images are placed in subfolders starting with the first three digits of the article_id; note, not all article_id values have a corresponding image.
- articles.csv - detailed metadata for each article_id available for purchase
- customers.csv - metadata for each customer_id in dataset
- sample_submission.csv - a sample submission file in the correct format
- transactions_train.csv - the training data, consisting of the purchases each customer for each date, as well as additional information. Duplicate rows correspond to multiple purchases of the same item. Your task is to predict the article_ids each customer will purchase during the 7-day period immediately after the training data period.

# Business Problem or Opportunity, Domain Knowledge

Link to domain data and need for this opportunity: [https://hmgroup.com/our-stories/plugged-in-how-hm-group-collaborates-with-the-tech-community/](https://hmgroup.com/our-stories/plugged-in-how-hm-group-collaborates-with-the-tech-community/)

## Business Problem/Opportunity: Improving Personalized Fashion Recommendations

### Domain Knowledge:

- Fashion Retail: Understanding the dynamics of the fashion industry, including consumer preferences, fashion trends, and seasonality, is crucial for developing effective personalized fashion recommendations. This may involve analyzing historical fashion data, studying fashion trends, and understanding customer behavior in the fashion retail context.
- Customer Segmentation: Segmenting customers based on their demographics, preferences, and behavior can provide valuable insights for developing personalized fashion recommendations. This may involve clustering techniques, such as k-means clustering or hierarchical clustering, to group similar customers based on their purchasing patterns, browsing behavior, or engagement with fashion products.
- Recommendation Systems: Familiarity with different types of recommendation algorithms, such as collaborative filtering, content-based filtering, or hybrid approaches, can help in developing effective personalized fashion recommendation systems. This may involve analyzing user-item interactions, item attributes, and other relevant features to generate personalized recommendations based on user preferences, browsing history, or past purchase behavior.
- Data Preprocessing and Feature Engineering: Understanding how to preprocess and engineer relevant features from the dataset, such as customer demographics, product attributes, purchase history, and browsing behavior, is critical for building accurate and meaningful personalized fashion recommendation models. This may involve data cleaning, feature extraction, normalization, or encoding techniques
- Evaluation Metrics: Familiarity with appropriate evaluation metrics, such as precision, recall, F1-score, or ranking-based metrics like precision at k or normalized discounted cumulative gain (NDCG), can help in evaluating the performance of personalized fashion recommendation models. This may involve comparing different algorithms or models based on their performance metrics to identify the best-performing recommendation system.

##  Research Objectives and Question(s) (what you are trying to describe or predict with the data)

The team formulated research questions that guide their analysis and investigation. These questions are aligned with their research objectives and are designed to address the business problem or opportunity identified. For example, "What are the key factors that influence customer preferences and purchasing decisions in the fashion industry?", "How accurate can we predict customer preferences and behaviors using different machine learning algorithms?", and "What strategies can be developed to improve personalized fashion recommendations and drive customer engagement and conversion?", “Do customers buy items they bought before?”

## Second Choice :

# Selection of data to analyze

The dataset includes information about ~73,000 Scrabble games played by three bots on Woogles.io: BetterBot (beginner), STEEBot (intermediate), and HastyBot (advanced). The games are between the bots and their opponents who are regular registered users. You are using metadata about the games as well as turns in each game (i.e., players' racks and where and what they played, AKA gameplay) to predict the rating of the human opponents in the test set (test.csv). You will train your model on gameplay data from one set of human opponents to make predictions about a different set of human opponents in the test set.

There is metadata for each game (games.csv), gameplay data about turns played by each player in each game (turns.csv), and final scores and ratings from BEFORE a given game was played for each player in each game (train.csv and test.csv).

Here is an example of a game played on woogles.io: https://woogles.io/game/icNJtmxy. Use the "Examine" button to replay the game turn-by-turn.


Kaggle Link: [https://www.kaggle.com/competitions/scrabble-player-rating/overview](https://www.kaggle.com/competitions/scrabble-player-rating/overview)

## Files:
This project aims to predict the rating of human opponents in Scrabble games played on Woogles.io based on metadata and gameplay data. The dataset includes information about approximately 73,000 games played by three bots (BetterBot, STEEBot, and HastyBot) against regular registered users. The dataset is divided into several CSV files, including games.csv, turns.csv, train.csv, and test.csv.

# Dataset Description
### games.csv
This file contains metadata about games, including the following columns:

- game_id: Unique id for the game
- first: Which player went first
- time_control_name: Name of time control used ("regular", "rapid", or "blitz")
- game_end_reason: How the game ended
- winner: Who won the game
- created_at: When the game was created
- lexicon: English lexicon used in the game ("CSW19", "NWL20", "CSW21")
- initial_time_seconds: Time limit each player has in the game (defines the time control name)
- increment_seconds: Time increment each player gets each time they play a turn
- rating_mode: Whether the game counts towards player ratings or not ("RATED", "CASUAL")
- max_overtime_minutes: How far past the initial time limit players can go before they timeout
- game_duration_seconds: How long the game lasted

### turns.csv
This file contains gameplay data about turns played by each player in each game, including the following columns:

- game_id: Unique id for the game
- turn_number: The turn number in the game
- nickname: Player's username on woogles.io
- rack: Player's current rack
- location: Where the player places their turn on the board (NA for games in the test set or if the player didn't make a play, e.g., if they exchanged)
- move: Tiles the player laid (NA for games in the test set; "--" if the turn_type was "Pass"; "(challenge)" if the turn_type was "Challenge"; "-" plus tiles exchanged if the turn_type was "Exchange"; at the end of the game, remaining tiles in a player's rack are in parentheses)
- points: Points the player earned (or lost) in their turn
- score: Player's total score at the time of the turn
- turn_type: Type of turn played ("Play", "Exchange", "Pass", "Six-Zero Rule" (i.e., a game that ends when players pass 3 turns in a row each), "Challenge")

### train.csv and test.csv
These files contain final scores and ratings from BEFORE a given game was played for each player in each game, including the following columns:

- game_id: Unique id for the game
- nickname: Player's username on woogles.io
- score: Final score for each player for each game
- rating: Player's rating on woogles.io BEFORE the game was played; ratings are per Lexicon / time control name (AKA game variant). In test.csv, ratings are NA for player games; this is what you are predicting.

### Objective
The objective of this project is to build a predictive model that can accurately predict the rating of human opponents in the test set (test.csv) based on the provided metadata and gameplay data. The model will be trained on gameplay data from one set of human opponents in the train set (train.csv) and evaluated on its ability to predict the ratings of a different set of human opponents in the

# Business Problem or Opportunity, Domain Knowledge

Link to domain data: [https://www.coololdgames.com/tile-games/scrabble/](https://www.coololdgames.com/tile-games/scrabble/)

## Business Problem/Opportunity: Scrabble Player Rating

### Domain Knowledge:


- Player performance analysis: You can use the dataset to analyze the performance of Scrabble players, such as their win/loss ratio, average scores, word choices, and game strategies. This can help identify patterns and trends in player performance, and potentially uncover areas for improvement or optimization.

- Player rating system evaluation: Scrabble has a rating system that assigns a numerical value to each player based on their performance. You can use the dataset to evaluate the effectiveness of the current rating system, identify any biases or inconsistencies, and propose potential modifications or enhancements to the rating system.

- Strategy analysis: Scrabble is a game that requires strategic thinking and word choice decisions. You can use the dataset to analyze the strategies used by players, such as high-scoring word choices, tile placements, and defensive or offensive moves. This can provide insights into the most effective strategies and tactics used in Scrabble games.

- Player behavior analysis: The dataset can also be used to analyze player behavior, such as playing styles, word preferences, and game patterns. This can help identify common behaviors or trends among players and provide insights into player preferences, habits, and strategies.

- Tournament performance analysis: Scrabble tournaments are organized at various levels, from local to international competitions. You can use the dataset to analyze the performance of players in Scrabble tournaments, identify factors that influence tournament success, and uncover potential strategies for improving tournament performance.


##  Research Objectives and Question(s) (what you are trying to describe or predict with the data)

Based on the domain knowledge and potential business problem or opportunity identified from the "Scrabble Player Rating" dataset, the following research objectives and questions can be formulated:

- Research Objective 1: Evaluate the relationship between player ratings and player performance in Scrabble.Research Question 1: How do player ratings impact player performance in terms of win/loss ratio, average scores, and game outcomes?


- Research Question 2: Are there any biases or inconsistencies in the current rating system, and how can it be improved to provide more accurate and fair player ratings?Research Objective 2: Assess the effectiveness of the current Scrabble rating system and propose potential modifications or enhancements.



- Research Question 3: What are the common strategies used by Scrabble players, such as word choices, tile placements, and defensive/offensive moves, and which strategies are associated with higher scores or win rates?Research Objective 3: Analyze the strategies used by Scrabble players and identify the most effective strategies for high performance.


- Research Question 4: What are the common player behaviors, playing styles, and word preferences in Scrabble games, and how do they impact player performance?Research Objective 4: Understand player behaviors and preferences in Scrabble games.


- Research Question 5: What factors, such as player ratings, playing styles, strategies, and tournament formats, influence the performance of players in Scrabble tournaments, and how can tournament performance be improved?Research Objective 5: Analyze the performance of players in Scrabble tournaments and identify factors that influence tournament success.

