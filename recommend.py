import tree
import json
from flask import Flask, render_template,request
import statistics
import plotly.graph_objs as go

app=Flask(__name__,static_folder="static")

# load the four attribute trees from jsonfiles
valenceTree=tree.Tree("valenceTree.json")
energyTree=tree.Tree("energyTree.json")
danceabilityTree=tree.Tree("danceabilityTree.json")
tempoTree=tree.Tree("tempoTree.json")

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

def getRecommendation(valence,energy,tempo,danceability):
    valence_list=[]
    energy_list=[]
    tempo_list=[]
    danceability_list=[]

    #get all songs that fit the valence crtiria from the valenceTree
    if valence=="low":
        valence_list=valenceTree.getRange(0,0.4)
    elif valence=="medium":
        valence_list=valenceTree.getRange(0.4,0.6)
    else:
        valence_list=valenceTree.getRange(0.6,10)

    #get all songs that fit the energy crtiria from the energyTree
    if energy=="low":
        energy_list=energyTree.getRange(0,0.4)
    elif energy=="medium":
        energy_list=energyTree.getRange(0.4,0.6)
    else:
        energy_list=energyTree.getRange(0.6,10)

    #get all songs that fit the tempo crtiria from the tempoTree
    if tempo=="low":
        tempo_list=tempoTree.getRange(0,100)
    elif tempo=="medium":
        tempo_list=tempoTree.getRange(100,130)
    else:
        tempo_list=tempoTree.getRange(130,1000)

    #get all songs that fit the danceability crtiria from the danceabilityTree
    if danceability=="low":
        danceability_list=danceabilityTree.getRange(0,0.4)
    elif danceability=="medium":
        danceability_list=danceabilityTree.getRange(0.4,0.6)
    else:
        danceability_list=danceabilityTree.getRange(0.6,10)

    recommend_index_list=list(set(valence_list)&set(energy_list)&set(tempo_list)&set(danceability_list))
    recommend_song_list=[]
    for i in recommend_index_list:
        recommend_song_list.append(all_song_list[i])
    return recommend_song_list
    

@app.route("/")
def index():
    return render_template("recommend_main.html")



@app.route("/recommend_result",methods=['POST'])
def recommend_result():
    valence=request.form["valence"]
    energy=request.form["energy"]
    tempo=request.form["tempo"]
    danceability=request.form["danceability"]
    recommend_song_list=getRecommendation(valence,energy,tempo,danceability)
    return render_template("recommend_result.html",result=recommend_song_list)

@app.route("/trend_result",methods=['POST'])
def trend_result():
    attribute=request.form["attribute"]
    x_vals=[str(x) for x in range(2010,2022)]
    y_vals=[]
    if attribute=="tempo":
        for year in range(2010,2022):
            y_vals.append(statistics.mean([song["tempo"] for song in song_dict[str(year)]]))
    elif attribute=="danceability":
        for year in range(2010,2022):
            y_vals.append(statistics.mean([song["danceability"] for song in song_dict[str(year)]]))
    elif attribute=="energy":
        for year in range(2010,2022):
             y_vals.append(statistics.mean([song["energy"] for song in song_dict[str(year)]]))
    else:
        for year in range(2010,2022):
            y_vals.append(statistics.mean([song["valence"] for song in song_dict[str(year)]]))
    
    bars_data=go.Bar(x=x_vals,y=y_vals)
    layout=go.Layout(title=f"Average {attribute} for Top-100 songs from 2010 to 2021")
    fig=go.Figure(data=bars_data,layout=layout)
    div=fig.to_html(full_html=False)
    return render_template("trend_result.html",plot_div=div)


if __name__=="__main__":
    app.run(debug=True)