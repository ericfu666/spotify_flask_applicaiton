import json
import random
import tree

# load song_dict from json file
file=open("song_dict.json","r")
json_file=file.read()
song_dict=json.loads(json_file)
file.close()

# load all_song_list from json file
file=open("all_song_list.json","r")
json_file=file.read()
all_song_list=json.loads(json_file)
file.close()

# create 4 trees for four song attributes: valence, energy, danceability, tempo
valenceTree=tree.Tree()
energyTree=tree.Tree()
danceabilityTree=tree.Tree()
tempoTree=tree.Tree()

# insert each song into the four trees 
# key=i (index in the all_song_list) ; val=song attribute score
for i in range(len(all_song_list)):
    valenceTree.put(i,all_song_list[i]["valence"])
    energyTree.put(i,all_song_list[i]["energy"])
    danceabilityTree.put(i,all_song_list[i]["danceability"])
    tempoTree.put(i,all_song_list[i]["tempo"])

# save the four trees as jsonfile
valenceTree.saveTree("valenceTree.json")
energyTree.saveTree("energyTree.json")
danceabilityTree.saveTree("danceabilityTree.json")
tempoTree.saveTree("tempoTree.json")