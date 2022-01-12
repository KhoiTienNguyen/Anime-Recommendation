# Anime-Recommendation

Anime Recommendation System using data collected from Jikan's unofficial MyAnimeList API v3. Used sklearn Python library to apply k-nearest-neighbour algorithm to train a recommendation model for all titles (up to 26th of July, 2021) on myanimelist.com. Type in any title on MyAnimeList to get 10 closest recommendations.

# Instructions to use

If all you need is the recommendation system, then only `src/recommendation.py`, `data/anime.csv`, and `data/users.csv` is needed to run.

#### get_users_from_clubs.py
- Collects a list of usernames from specified clubs to a .txt file
- usage: ```get_users_from_clubs.py  [-h] -o OUTPUT```
- Example: ```get_users_from_clubs.py -o usernames.txt```

#### get_user_ratings.py
- Collects user ratings from list of usernames generated from `get_users_from_clubs.py`
- Outputs numbered and segmented .json files starting with index of FILE_COUNT, each with a specified number of users
- usage: ```get_user_ratings.py  [-h] -o OUTPUT -i INPUT -c FILE_COUNT -n NUMBER_OF_USERS_PER_FILE```
- Example: ```get_user_ratings.py -o users.json -i usernames.txt -c 1 -n 500```

#### collect_all_anime.py
- Collects all anime and their relevant information from a specified range of anime ID
- Outputs numbered and segmented .json files starting with index of FILE_COUNT, each with a specified number of titles
- usage: ```collect_all_anime.py  [-h] -o OUTPUT -s START_ID -e END_ID -c FILE_COUNT -n NUMBER_OF_ANIME_PER_FILE```
- Example: ```collect_all_anime.py -o anime.json -s 1 -e 54000 -c 1 -n 100```

#### combine_json.py
- Outputs a combined .json file from the numbered and segmented .json files generated from `get_users_from_clubs.py` and `collect_all_anime.py`
- Specify the file format of the segmented .json files and specify the first and last index of the files to be combined
- usage: ```combine_json.py  [-h] -i INPUT_FILE_FORMAT -o OUTPUT -s START_INDEX -e END_INDEX```
- Example: ```combine_json.py -i users.json -o combined_users.json -s 1 -e 30```

#### users_json_to_csv.py
- Converts combined_users.json generated from `combine_json.py` to suitable .csv format for `recommendation.py` to use
- usage: ```users_json_to_csv.py  [-h] -o OUTPUT -i INPUT```
- Example: ```users_json_to_csv.py-o combined_users.csv -i combined_users.json```

#### anime_json_to_csv.py
- Converts combined_users.json generated from `combine_json.py` to suitable .csv format for `recommendation.py` to use
- usage: ```anime_json_to_csv.py  [-h] -o OUTPUT -i INPUT```
- Example: ```anime_json_to_csv.py -o combined_anime.csv -i combined_anime.json```

#### recommendation.py
- Gives anime recommendations
- If no input .pkl model is inputted, you will have to specify the output path to the generated model.
- usage: ```recommendation.py  [-h] (-o OUTPUT_MODEL | -i INPUT_MODEL) -a ANIME_CSV -u USERS_CSV```
- Example: ```recommendation.py -o knn_model.pkl -a combined_anime.csv -u combined_users.csv```

# To do
- Add option to filter by genre, age rating, type (eg. TV, Movie,...), popularity
- Collect more users for more accurate recommendations (currently ~ 15k users collected)