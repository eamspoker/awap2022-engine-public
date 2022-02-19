import sys

import random

from src.player import *
from src.structure import *
from src.game_constants import GameConstants as GC

class MyPlayer(Player):

    def __init__(self):
        print("Init")
        self.turn = 0

        return


    def play_turn(self, turn_num, map, player_info):
        openList = []
        closedList = []



        return


    def rank(self, tile, map):
        currX = tile.x
        currY = tile.y
        if (currX > 0):
            tile1 = map[currX - 1][currY]
            if(currY > 0):
                tile2 = map[currX - 1][currY-1]
        if(currY > 0):
            