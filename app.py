from flask import Flask, request, render_template, render_template_string

from models.match import *
# from models.over import *
from models.team import *
  
app = Flask(__name__)
# global match_
  
@app.route('/')
def index():
    print("hello")
    return render_template("index.html") 


@app.route('/dashboard', methods=['POST'])
def dashboard():

    global match_

    teamA_name = request.form['teamA']
    teamB_name = request.form['teamB']

    teamA_player_count = int(request.form['teamAn'])
    teamA_players = []

    for i in range(1, teamA_player_count + 1) :
        teamA_players.append(request.form['teamA' + str(i)])

    teamB_player_count = int(request.form['teamBn'])
    teamB_players = []

    for i in range(1, teamB_player_count + 1) :
        teamB_players.append(request.form['teamB' + str(i)])

    first = request.form['first']
    overs = request.form['overs']

    if first == teamA_name : 
        first = 'A'
    else : 
        first = 'B'

    teamA = Team(teamA_name, teamA_players, teamA_player_count)
    teamB = Team(teamB_name, teamB_players, teamB_player_count)
    match_ = Match(teamA, teamB, overs, first)

    glossary = ["Player Name : Score : 4s : 6s : Balls"]
    glossary_count = 0

    if first == 'A' : 
        glossary_count = teamA_player_count + 1
        for i in teamA_players :
            glossary.append(i + " : 0 : 0 : 0 : 0 ")
    else : 
        glossary_count = teamB_player_count + 1
        for i in teamB_players :
            glossary.append(i + " : 0 : 0 : 0 : 0 ")
    


    return render_template("dashboard.html", 
                glossary = glossary, 
                glossary_rows = glossary_count,
                current_over = 1,
                current_bowler = "",
                score = ""
                ) 

@app.route('/refresh', methods=['POST'])
def refresh():

    over = request.form['over']
    bowler = request.form['bowler']

    match_.number_of_overs += 1
    match_.current_bowler = bowler
    
    over_score = 0
    for i in over.split(" "):
        over_score += int(i)

    current_score = 0

    match_.overs.append(over)
    if match_.innings == 1 and match_.first_batter == 'A' :
        match_.runs_A += over_score
        current_score = match_.runs_A
    else : 
        match_.runs_B += over_score
        current_score = match_.runs_B
        

    glossary = "Player Name \t\t Score\t\t 4s \t\t 6s \t\t Balls" 

    if first == 'A' : 
        for i in teamA_players :
            glossary += i + "\t\t 0 \t\t 0 \t\t 0 \t\t 0"
    else : 
        for i in teamB_players :
            glossary += i + "\t\t 0 \t\t 0 \t\t 0 \t\t 0"

    return render_template("dashboard.html", 
                glossary = glossary, 
                glossary_rows = glossary_count,
                current_over = match_.number_of_overs + 1,
                current_bowler = bowler,
                score = current_score
                ) 



@app.route('/about')
def about():
    return render_template("about.html") 
  

if __name__ == "__main__":
    app.run(debug=True)