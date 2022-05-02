# from models.player import Player
from models.player import Player

from typing import Iterable

class Team :

    name = None
    players = [None] * 11 #Player type
    player_count = None

    # Batting 
    total_runs = None
    wickets_down = None

    # Bowling
    wickets_taken = None
    runs_conceded = None

    def __init__(self, name, players) :
        self.name = name
        self.players = players

    def __init__(self, name, players, player_count) :
        self.player_count = player_count
        self.name = name
        self.players = players
