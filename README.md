# SoccerBetting

The project has been complicated in the sense that there has been a lot of moving parts and a lot of different team members have worked on different parts of the project. Here is the breakdown of the important files and folders and what it represents:

* data/fbref_scraper    -    Contains code for scraping data from fbref. 
* data/fbref_scraper/per_game_match_reports    -    Contains code for scraping per game report from fbref + implementations multiprocessing, multithreading, Numba, Cython optimization attempts
* data/fbref_scraper/per_game_match_reports    -    Contains code for scraping per player game match report from fbref + usage of disk cache + Merging these data
* data/fivethirtyeight    -    Contains the downloaded data from FiveThirtyEight's website + Code to reformat the data to make it look the same as the fbref data (needed later for merging)
* data/football-data.co.uk    -    Contains the dowloaded data from 'football-data.co.uk' + Code to merge data for each season and each league to one final dataset + Code to reformat the data to make it look the same as the fbref data (needed later for merging, this is where Just in time compilation was tried to speedup levenshtein ratio and distance calculation to match team names with fbref names).
* data/understat_scraper    -    Contains code to scrape data from Understat + Code to reformat the data to make it look the same as fbref data (needed later for merging)
* final_data    -    Contains folder for all data sources final datasets + Contains code to merge all datasets from all the sources + Contains code to implement Colley's Rating System.
* models/game_prediction    -    Contains code to model the problem as binary and multi-class classification and find best features.
* models/neural_rating_system_models    -    Contains code to build the neural network for building the neural rating system using multiple methods. Code for final models that were trained are in "OD Ratings - An Optimization Approach.ipynb", "OD Ratings - HFA approach.ipynb"