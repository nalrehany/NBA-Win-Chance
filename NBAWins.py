from nba_api.stats.endpoints import scoreboard
import pandas as pd 
import time


# Set a date range for games played
date_range = pd.date_range('2015-03-15', '2015-03-16')

# Create a data frame for iterated data to be appended to
full_range_scores = pd.DataFrame()

# Loop to sort through games. 
for date in date_range:
   
    # Endpoint of api to be used. In this case, it is scoreboard
    game_scores_raw = scoreboard.Scoreboard(game_date = date)
    
    # Ensure time in between api calls
    time.sleep(.600)

    # Data comes in smaller data frames. Necessary to extract the desired one
    game_scores = game_scores_raw.get_data_frames()[1]
    
    # Create a column contianing teams' scores going into 4th quarter of a game
    game_scores['score_into_4th'] = game_scores['PTS_QTR1'] + game_scores['PTS_QTR2'] + game_scores['PTS_QTR3'] 

    # Only retain relevant variables
    game_scores = game_scores[['GAME_DATE_EST','GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PTS', 'score_into_4th']]
    
    # Unstack and widen data
    game_scores = game_scores.set_index(['GAME_ID', game_scores.groupby('GAME_ID').cumcount()+1]).unstack()
    game_scores.columns=[f'{i}_{j}' for i, j in game_scores.columns]
    game_scores.reset_index()
    
    # Append the date's game data to a new dataframe
    full_range_scores = full_range_scores.append(game_scores)
