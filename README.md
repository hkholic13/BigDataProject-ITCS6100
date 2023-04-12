# BigDataProject-ITCS6100

# Team

## Members:
- Ramya Jampani
- Chetan Subhash Chunduru
- Himanshi Khatri
- Revanth Kumar Galla
- Satya Sai Rajesh Parvatareddy

## Communication plan to include project artifact repository:
Methods of communication :- e-mail, in-person(once a week)

Communication response times:- Same day

Meeting attendance:- After looking into everyone’s schedule we had decided to meet every Wednesday either virtual or in-person to discuss the progress of the project and attendance to this is mandatory.

Running meetings:- Virtual

Meeting preparation: We decided to come prepared to the meetings so that we can use the time in the most efficient way.

Version control: By creating pull requests, team members can push all of their modifications to the artifact, which are then assessed by their peers and merged. 
Git link(https://github.com/hkholic13/BigDataProject-ITCS6100)

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

- Fashion Retail: In order to offer customized fashion suggestions, it is crucial to possess a comprehensive comprehension of the fashion industry's workings, including factors such as shopper preferences, fashion trends, and seasonal variations. This entails investigating past fashion data, staying up-to-date with current trends, and comprehending customer behavior while shopping for apparel.
- Customer Segmentation: Customers can be classified based on their demographics, preferences, and behaviors, which can be used to create tailored fashion recommendations. Using clustering methods such as k-means or hierarchical clustering to group similar customers based on their shopping habits, browsing activity, or interaction with fashion items may be part of this process.
- Recommendation Systems: Having knowledge about diverse recommendation algorithms, such as collaborative filtering, content-based filtering, and hybrid methods, can assist in creating proficient personalized fashion recommendation systems. This could require examining user-item interactions, item qualities, and other relevant features to create Customized guidance based on the user's preferences, browsing history, or past purchasing behavior.
- Data Preprocessing and Feature Engineering: Understanding how to preprocess and engineer relevant features from the dataset, such as customer demographics, product attributes, purchase history, and browsing behavior, is critical for building accurate and meaningful personalized fashion recommendation models. This may involve data cleaning, feature extraction, normalization, or encoding techniques
- Evaluation Metrics: When evaluating the performance of personalized fashion recommendation models, it can be helpful to have a working knowledge of appropriate evaluation metrics. Some examples of these metrics include precision, recall, and F1-score. Ranking-based metrics, such as precision at k or normalized discounted cumulative gain (NDCG), are also examples. This may involve comparing different algorithms or models based on their performance metrics to identify the best-performing recommendation system.

##  Research Objectives and Question(s) (what you are trying to describe or predict with the data)

The team formulated research questions that guide their analysis and investigation. These questions align with their research objectives and are intended to address the identified business challenge or opportunity.
For example, "What are the key factors that influence customer preferences and purchasing decisions in the fashion industry?", "How accurate can we predict customer preferences and behaviors using different machine learning algorithms?", and "What strategies can be developed to improve personalized fashion recommendations and drive customer engagement and conversion?", “Do customers buy items they bought before?”
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

-game_id: Unique id for the game
-first: Which player went first
-time_control_name: Name of time control used ("regular", "rapid", or "blitz")
-game_end_reason: How the game ended
-winner: Who won the game
-created_at: When the game was created
-lexicon: English lexicon used in the game ("CSW19", "NWL20", "CSW21")
-initial_time_seconds: Time limit each player has in the game (defines the time control name)
-increment_seconds: Time increment each player gets each time they play a turn
-rating_mode: Whether the game counts towards player ratings or not ("RATED", "CASUAL")
-max_overtime_minutes: How far past the initial time limit players can go before they timeout
-game_duration_seconds: How long the game lasted

### turns.csv
This file contains gameplay data about turns played by each player in each game, including the following columns:

-game_id: Unique id for the game
-turn_number: The turn number in the game
-nickname: Player's username on woogles.io
-rack: Player's current rack
-location: Where the player places their turn on the board (NA for games in the test set or if the player didn't make a play, e.g., if they exchanged)
-move: Tiles the player laid (NA for games in the test set; "--" if the turn_type was "Pass"; "(challenge)" if the turn_type was "Challenge"; "-" plus tiles exchanged if the turn_type was "Exchange"; at the end of the game, remaining tiles in a player's rack are in parentheses)
-points: Points the player earned (or lost) in their turn
-score: Player's total score at the time of the turn
-turn_type: Type of turn played ("Play", "Exchange", "Pass", "Six-Zero Rule" (i.e., a game that ends when players pass 3 turns in a row each), "Challenge")
-train.csv and test.csv
These files contain final scores and ratings from BEFORE a given game was played for each player in each game, including the following columns:

-game_id: Unique id for the game
-nickname: Player's username on woogles.io
-score: Final score for each player for each game
-rating: Player's rating on woogles.io BEFORE the game was played; ratings are per Lexicon / time control name (AKA game variant). In test.csv, ratings are NA for player games; this is what you are predicting.

Objective
This project's objective is to develop a predictive model that can accurately predict the ratings of human opponents in the test set (test.csv) by utilizing provided metadata and gameplay data. The model will be trained on gameplay data of a separate group of human opponents in the train set (train.csv) and assessed on its proficiency in predicting the ratings of another distinct group of human opponents.

# Business Problem or Opportunity, Domain Knowledge

Link to domain data: [https://www.coololdgames.com/tile-games/scrabble/](https://www.coololdgames.com/tile-games/scrabble/)

## Business Problem/Opportunity: Scrabble Player Rating

### Domain Knowledge:


- Player performance analysis: By utilizing the dataset, you can scrutinize the proficiency of Scrabble players, which includes their average score, win/loss ratio, word preferences, and game tactics. This process can assist in detecting trends and patterns in player performance and identifying possible areas for improvement or optimization.

- Player rating system evaluation: Scrabble utilizes a rating system that assigns a numeric value to each player based on their game performance. By utilizing the dataset, you can appraise the efficiency of the existing rating system, detect any biases or inconsistencies, and suggest alterations or enhancements to strengthen the rating system.

- Strategy analysis: Scrabble is a game that involves selecting words strategically, and analyzing the dataset can help understand the strategies that players use. These strategies may include choosing words that yield high scores, placing tiles effectively, and making defensive or offensive moves. Examining this data could provide valuable insights into the most effective tactics and strategies to use in Scrabble.

- Player behavior analysis: Through a thorough analysis of the dataset, it becomes feasible to explore how Scrabble players approach the game, which words they favor, and their game patterns. Such an analysis can help to identify any typical behaviors or trends among players and offer insightful knowledge regarding their methods, inclinations, and habits.

- Tournament performance analysis: Scrabble tournaments are arranged across various levels, ranging from regional to international contests. The dataset can be utilized to conduct an analysis of players' performance in Scrabble tournaments, ascertain the factors that impact tournament success, and reveal prospective strategies for enhancing tournament performance.


##  Research Objectives and Question(s) (what you are trying to describe or predict with the data)

Based on the domain knowledge and potential business problem or opportunity identified from the "Scrabble Player Rating" dataset, the following research objectives and questions can be formulated:

- Research Objective 1: Evaluate the relationship between the ratings of Scrabble players and their corresponding level of performance. Research Question 1: To what extent do player ratings affect their win/loss ratio, average scores, and game outcomes? Research Question 2: How can the Scrabble rating system be improved to provide more accurate and impartial player ratings, ensuring fairness and consistency?

- Research Objective 2: Explore opportunities to enhance the Scrabble rating system for even better results.


- Research Question 3: What are the effective tactics utilized by Scrabble players, such as word choices, tile placements, and defensive/offensive moves, and which strategies are associated with higher scores or win rates? Research Objective 3: Explore the strategies utilized by Scrabble players and discover the most effective tactics for achieving exceptional performance.


- Research Question 4: How can understanding common playing styles, word preferences, and player behaviors in Scrabble games positively impact player performance? Research Objective 4: Discover exciting insights into Scrabble players' preferences, behaviors, and playing styles.

- Research Question 5: How can players improve their performance in Scrabble tournaments by considering factors such as player ratings, playing styles, strategies, and tournament formats? Research Objective 5: Explore the factors that contribute to success in Scrabble tournaments and identify strategies for improving performance.

