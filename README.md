# NBA Win Chance
This small program finds the chance based on over 21,000 NBA games that an NBA team will win a game if winning by 10+ points going into the 4th quarter of play.
This idea was inspired by a NBA junky friend of mine, and seemed simple enough to produce given available data. Thanks to Ken Jee's NBA API that parses official NBA stats, this project utilized the API and a little bit of manipulation to access the correct form of data I needed. 
	
## What Was Used

* Python 3.9
* nba_api by Ken Jee
* Pandas
* time
	
## Using the API
nba_api utilizes endpoints that contain different families of basketball statistics. For example, in this project, the scores after each quarter were required, leading to the use of the scoreboard endpoint. However, there exists endpoints for virtually any family of statistics ranging from the defensive stats of a player in a certain game to something more general like franchise leaders. 

### Note
I found that using a break in between API calls of .6 of a second: ```time.sleep(.600)``` worked ideally for not being too greedy with the server. 
