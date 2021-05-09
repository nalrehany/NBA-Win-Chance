from nba_api.stats.endpoints import scoreboard
import pandas as pd 
import time
import numpy as np

# Set a date range for games played
dates = pd.date_range('2015-10-25', '2018-07-05')

# Create a data frame for iterated data to be appended to
full_range_scores = pd.DataFrame()

# Loop to sort through games
for date in dates:
   
    print(date)
     
    # Endpoint of api to be used. In this case, it is scoreboard
    game_scores_raw = scoreboard.Scoreboard(game_date = date)
    
    # Ensure time in between api calls
    time.sleep(.600)

    # Data comes in smaller data frames. Necessary to extract the desired one
    game_scores = game_scores_raw.get_data_frames()[1]
    
    # Skip over days where no games are played
    if game_scores.empty == True:
        continue
    
    # Create a column containing teams' scores going into 4th quarter of a game
    game_scores['score_into_4th'] = game_scores['PTS_QTR1'] + game_scores['PTS_QTR2'] + game_scores['PTS_QTR3'] 

    # Only retain relevant variables
    game_scores = game_scores[['GAME_DATE_EST','GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PTS', 'score_into_4th']]

    # Create home and visiting team records
    g = game_scores.groupby('GAME_ID').cumcount()
    home_team = game_scores.set_index(['GAME_ID', g + 1])
    visiting_team = game_scores.set_index(['GAME_ID', 2 - g])

    home_team = home_team.unstack()
    home_team.columns = [f'{i}_{j}' for i, j in home_team.columns]

    visiting_team = visiting_team.unstack()
    visiting_team.columns = [f'{i}_{j}' for i, j in visiting_team.columns]

    # Concatenate home and visiting records
    game_scores = pd.concat([home_team, visiting_team]).sort_index().reset_index()
    
    # Create a column containing 'W' or 'L' for one of the teams in each game
    # This allows for comparison of game result with +/- after 3 quarters
    game_scores['Team1_W/L'] = np.where(game_scores['PTS_1'] > game_scores['PTS_2'], 'W', 'L')
    
    # Create a column contianing the +/- of the lead or deficit after 3 quarters
    game_scores['plusminus_after_3'] = game_scores['score_into_4th_1'] - game_scores['score_into_4th_2']
    
    # Append the date's game data to a new dataframe
    full_range_scores = full_range_scores.append(game_scores)

# Filter for the number of games where a team was leading by 10+ points going into the 4th    
up_10_after_3 = full_range_scores[full_range_scores['plusminus_after_3'] >= 10]
length1 = len(up_10_after_3)

# Filter for the number of games where a team was leading by 10+ points going into the 4th and won
up_10_after_3_W = up_10_after_3[up_10_after_3['Team1_W/L'] == 'W']
length2 = len(up_10_after_3_W)

# Divide and find final percentage
final_percentage = length2/length1
