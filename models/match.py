from models.team import Team

class Match : 
    
    teamA = None                #Team type
    teamB = None                #Team type

    overs = None
    number_of_overs = None
    first_batter = None                 # A or B

    current_batter_1 = None     #Index from lineup array
    current_batter_2 = None     #Index from lineup array
    current_bowler = None       #Index from lineup array

    runs_A = None               
    runs_B = None

    wickets_A = None
    wickets_B = None

    innings = 1


    def __init__(self, teamA : Team, teamB : Team) :

        self.teamA = teamA
        self.teamB = teamB
        self.overs = []
        self.runs_A = 0
        self.runs_B = 0
        self.wickets_A = 0
        self.wickets_B = 0
        self.current_batter_1 = 0
        self.current_batter_2 = 1
        self.innings = 1


    def __init__(self, teamA : Team, teamB : Team, overs, first_batter) :

        self.number_of_overs = overs
        self.first_batter = first_batter

        self.teamA = teamA
        self.teamB = teamB
        self.overs = []
        self.runs_A = 0
        self.runs_B = 0
        self.wickets_A = 0
        self.wickets_B = 0
        self.current_batter_1 = 0
        self.current_batter_2 = 1
        self.innings = 1



