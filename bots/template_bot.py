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
       priorityQueue = self.BFS(map, 0,0, [], [], [], player_info)
       return


    def getChild(i, j, dir, map):
        drow, dcol = dir
        return map[i+drow][j+dcol]

    def BFS(self, map, i, j, visited, priorityQueue, queue, player_info):
        queue.append(map[i][j])
        visited.append(map[i][j])

        dirs = [(1,0), (-1, 0), (0,1), (0, -1)]

        while queue != []:
            st1 = queue.pop(0).structure
            if st1 is not None & st1.team == player_info.team:
                for dir in dirs:
                    newNode = self.getChild(i, j, dir, map)
                    if newNode not in visited:
                        queue.append(newNode)
                        visited.append(newNode)
                        st = newNode.structure
                        if st is None:
                            priorityQueue.append(newNode)
            else:
                for dir in dirs:
                    newNode = self.getChild(i, j, dir, map)
                    if newNode not in visited:
                        queue.append(newNode)
                        visited.append(newNode)
        
        return priorityQueue

    

                




