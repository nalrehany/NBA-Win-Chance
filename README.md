# NBA Win Chance
This small program finds the chance based on over 21,000 NBA games that an NBA team will win a game if winning by 10+ points going into the 4th quarter of play.
This idea was inspired by a NBA junky friend of mine, and seemed simple enough to produce given available data. Thanks to Ken Jee's NBA API that parses official NBA stats, this project utilized the API and a little bit of manipulation to access the correct form of data I needed. 
	
## What Was Used

* Python 3.9
* * nba_api by Ken Jee
* * Pandas
* * time
* R
* * tidyverse
* * dplyr
	
## Using the API
nba_api utilizes endpoints that contain different families of basketball statistics. For example, in this project, the scores after each quarter were required, leading to the use of the scoreboard endpoint. However, there exists endpoints for virtually any family of statistics ranging from the defensive stats of a player in a certain game to something more general like franchise leaders. 

## Key Data Manipulations
I try to include ample commentary in my code, so I will mention here the notable manipulations I encountered for your learning and practice
* Widening the dataframe as the results of a game were shown in different rows, with each team and its respective score along with the shared GameID. Using ```groupby``` & ```cumcount``` then flattening the multiindex column, we are able to get the game results with both teams and there scores in the same row. Then utilizing ```unstack()```, we are able to have the same game in another row but with the teams swapped.

The reason for requiring this is because to find the percentage of winning a game when up 10+ going into the 4th quarter, we need to have all of the games present for the calculation. Therefore, we create 2 rows for each game, each row corresponding the result of each team in a given game.


### Note
I found that using a break in between API calls of .6 of a second: ```time.sleep(.600)``` worked ideally for not being too greedy with the server. 

The R program does not utilize the nba_api, but instead works with a smaller set of manually gathered game data to complete the same analysis.
