# Project Description
A flask-based website that recommends top Billboard songs from 2010 to 2021 based on users' preferences and also displays song trends over the years.

# Required packages:
bs4, requests, flask, plotly

# How to Run
Run the recommend.py file and follow the routes to see recommendations and trend plots.

# Routes
/ -> index route<br>
/recommend_result -> the page where users get song recommendations<br>
/trend_result -> the page where users can check song trend plots<br>
 
# Data source
I crawled and scraped the names and artist names of all Top-100 songs from 2010 to 2021 from the Billboard website. Having the basic information of the songs, I used Spotipy (a lightweight python library for accessing Spotify API that requires OAuth) to get the detailed information about audio features (tempo, danceability, valence, and energy) for each song. 

# Data structure
Because for the interaction part, users can choose different tempo, danceability, valence, and energy to get recommendations, I built four Binary Search Trees for all the Billboard songs (one for each song attribute). To get the recommendations, range searches are performed for all four Binary Search Trees, and then an intersection operation is used on the four returned lists to get the songs that fit all four criteria.

# In this Repository
<ul>
  <li>recommend.py -- the main function that runs the Flask app</li>
  <li>song_dict.py -- Billboard web scraping and Spotify API access to get the top songs from 2010 to 2021</li>
  <li>stats.py -- preliminary statistical check on the songs data (optional)</li>
  <li>tree.py -- defines Node class and Tree class for data storage</li>
  <li>songtree.py -- stores the songs into four trees according to tempo, danceability, valence, and energy</li>
  <li>song_dict.json -- jsonfile storing top-100 songs from 2010 to 2021 in a dictionary (e.g. song_dict["2013"] to access top-100 songs in 2013)</li>
  <li>all_song_list.json -- jsonfile storing all the top-100 songs from 2010 to 2021 as a single list</li>
  <li>valence.json -- jsonfile storing all top-100 songs from 2010 to 2021 as a tree based on valence score</li>
  <li>energy.json -- jsonfile storing all top-100 songs from 2010 to 2021 as a tree based on energy score</li>
  <li>danceability.json -- jsonfile storing all top-100 songs from 2010 to 2021 as a tree based on danceability score</li>
  <li>tempo.json -- jsonfile storing all top-100 songs from 2010 to 2021 as a tree based on tempo</li>
</ul>
