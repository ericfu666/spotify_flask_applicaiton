import requests
from bs4 import BeautifulSoup
import json

# set up spotipy to access spotify API
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid="a69123c75c4e45a19d998f88c0a60c0c"
secret="55d7717d23cf4e9a8de204e7d9e7a803"
auth_manager=SpotifyClientCredentials(client_id=cid,client_secret=secret)
sp=spotipy.Spotify(auth_manager=auth_manager)

def load_cache():
    try:
        cache_file = open("song_dict.json", 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache

def save_cache(cache):
    cache_file = open("song_dict.json", 'w')
    contents_to_write = json.dumps(cache)
    cache_file.write(contents_to_write)
    cache_file.close()

billboard_base_url="https://www.billboard.com/charts/year-end/"
# song dict for songs from 2010 to 2021
song_dict=load_cache()

for year in range(2010,2022):
    if str(year) not in song_dict.keys():
        song_dict[str(year)]=[]
        # scrape the billboard top-100 songs from 2010 to 2021 to the song_dict
        billboard_year_url=billboard_base_url+str(year)+"/hot-100-songs/"
        response=requests.get(billboard_year_url)
        html_text=response.text
        soup=BeautifulSoup(html_text,"html.parser")
        songName_soupList=soup.select("h3.c-title.a-font-primary-bold-s")
        artistName_soupList=soup.select("span.c-label.a-font-primary-s")
        for i in range(len(songName_soupList)):
            songName=str(songName_soupList[i].string).strip()
            artistName=str(artistName_soupList[i].string).strip()

            # search for track id by the track name and artist name
            # (try narrow and broad search because there are inconsistencies)
            track_narrow_result=sp.search(q="track: "+songName+" artist: "+artistName.split()[0],type="track")
            track_broad_result=sp.search(q="track: "+songName,type="track")
            if len(track_narrow_result["tracks"]["items"])>0:
                track_id=track_narrow_result["tracks"]["items"][0]["uri"]
            elif len(track_broad_result["tracks"]["items"])>0:
                track_id=track_broad_result["tracks"]["items"][0]["uri"]
            else:
                continue

            # check audio features by track id
            audio_feature=sp.audio_features(track_id)

            # create song as a dictionary
            song={}
            song["name"]=songName
            song["artist"]=artistName
            song["year"]=str(year)
            song["danceability"]=audio_feature[0]["danceability"]
            song["energy"]=audio_feature[0]["energy"]
            song["valence"]=audio_feature[0]["valence"]
            song["tempo"]=audio_feature[0]["tempo"]

            # append the song to the corresonpind year list in song_dict
            song_dict[str(year)].append(song)
        
        # save song_dict
        save_cache(song_dict)


# merge all the songs into a big list
all_song_list=[]
for year_list in song_dict.values():
    all_song_list+=year_list


cache_file = open("all_song_list.json", 'w')
contents_to_write = json.dumps(all_song_list)
cache_file.write(contents_to_write)
cache_file.close()










    
    

