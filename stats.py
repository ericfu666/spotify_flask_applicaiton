import json
import statistics

file=open("song_dict.json","r")
json_file=file.read()
song_dict=json.loads(json_file)
file.close()

# merge all the songs into a big list
all_song_list=[]
for year_list in song_dict.values():
    all_song_list+=year_list

# four song attribute
valence_list=[]
energy_list=[]
danceability_list=[]
tempo_list=[]

for song in all_song_list:
    valence_list.append(song["valence"])
    energy_list.append(song["energy"])
    danceability_list.append(song["danceability"])
    tempo_list.append(song["tempo"])

# check statistics
print(statistics.quantiles(valence_list, n = 3))
print(statistics.quantiles(energy_list, n = 3))
print(statistics.quantiles(danceability_list, n = 3))
print(statistics.quantiles(tempo_list, n = 3))

