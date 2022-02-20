import sys
import time
import random

from src.player import *
from src.structure import *
from src.game_constants import GameConstants as GC

class pq():
    def __init__(self):
        self.list = []
        self.max = 0
        return
    
    def pq_insert(self, x,y, kind, score):
        item = (x,y,kind,score)
        self.list.append(item)
        self.mergeSort(self.list)
    
    def pq_pop(self):
        if self.list == []:
            # print("NOT POPPUNG VERY SUCK")
            return None
        else:
            # print("POPPPPPPPPPPPPPPPPPPPP")
            return self.list.pop()

    def mergeSort(self, arr):
        if len(arr) > 1:
    
            # Finding the mid of the array
            mid = len(arr)//2
    
            # Dividing the array elements
            L = arr[:mid]
    
            # into 2 halves
            R = arr[mid:]
    
            # Sorting the first half
            self.mergeSort(L)
    
            # Sorting the second half
            self.mergeSort(R)
    
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i][3] < R[j][3]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

class MyPlayer(Player):

    def __init__(self):
        print("Init")
        self.turn = 0
        self.built = []

        return

    def costBenefit(self, map, player_info, tile, q):
        #Tile class members: 
        #x (int)
        #y (int)
        #passability (float) - the multiplicative cost of building on this tile
        #population (int) - number of people living on this tile
        #structure (Structure object) - structure built on this Tile, or None

        #check if we can build
        if (tile.x, tile.y) not in self.built and map[tile.x][tile.y].structure is None:
            towerCost = StructureType.TOWER.get_base_cost() * map[tile.x][tile.y].passability
            roadCost = StructureType.ROAD.get_base_cost() * map[tile.x][tile.y].passability

            #population of current tile
            population = tile.population

            tileList = [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (1, -1), (-1, -1), (-1, 1),
                        (2, 0), (-2, 0), (0, 2), (0, -2)]
            
            for dt in tileList:
                if(0 <= tile.x + dt[0] and tile.x + dt[0] < self.MAP_WIDTH):
                    if(0 <= tile.y + dt[1] and tile.y + dt[1] < self.MAP_HEIGHT):
                        population += map[tile.x + dt[0]][tile.y + dt[1]].population

            # check if my team can afford this structure
            if population > 0 and player_info.money >= towerCost:
                self.build(StructureType.TOWER, tile.x, tile.y)
                self.built.append((tile.x, tile.y))
            elif player_info.money-250 >= roadCost:
                q.pq_insert(tile.x, tile.y, "ROAD", player_info.money/roadCost)
        return



    def play_turn(self, turn_num, map, player_info):
        self.MAP_WIDTH = len(map)
        self.MAP_HEIGHT = len(map[0])
        init_q = pq()
        # print(f"initial: {init_q.list}")
        self.BFS(map, 0,0, [], init_q, [], player_info)
        # print(f"queue: {init_q.list}")
        # print(f"final: {init_q.list}")
        to_build = init_q.pq_pop()
        while(to_build != None):
            # print("BUILD: ")
            # print(map[to_build[1]][to_build[0]].structure)
            # print(init_q.list)
            if to_build == None:
                print("")
            elif (to_build[2] == "TOWER"):
                # print(f"tower????????? {to_build[1]}, {to_build[0]}")
                self.build(StructureType.TOWER, to_build[0], to_build[1])
                self.built.append((to_build[0], to_build[1]))
            else:
                # print("road!!!!!!!!!")
                self.build(StructureType.ROAD, to_build[0], to_build[1])
                self.built.append((to_build[0], to_build[1]))
            
            to_build = init_q.pq_pop()
        self.set_bid(3)
        # print(type(self._to_build[0]))
        return


    def getChild(self, x, y, dir, map):
        drow, dcol = dir
        if 0 <= x+dcol and x+dcol < self.MAP_WIDTH and 0 <= y + drow and y + drow < self.MAP_HEIGHT:
            return map[x+dcol][y+drow], x+dcol, y+drow
        return -1, -1, -1

    def BFS(self, map, x1, y1, visited, priorityQueue, queue, player_info):
        
        queue.append(map[x1][y1])
        visited.append((x1,y1))

        dirs = [(1,0), (-1, 0), (0,1), (0, -1)]
        while queue != [] and len(priorityQueue.list) < 10:
            start = queue.pop(0)
            st1 = start.structure
            # print(visited)
            if st1 is not None and st1.team == player_info.team:
                for dir in dirs:
                    newNode, x, y= self.getChild(start.x, start.y, dir, map)
                    # print(f"row of New: {row} col of New: {col}, value: {newNode}")
                    if newNode != -1:
                        # print("HERE")
                        if (x, y) not in visited:
                            visited.append((x, y))
                            queue.append(newNode)
                        st = newNode.structure
                        if st is None:
                           self.costBenefit(map, player_info, newNode, priorityQueue)
                        #    print(priorityQueue.list)
            else:
                for dir in dirs:
                    newNode, x, y = self.getChild(start.x, start.y, dir, map)
                    if newNode != -1 and (x, y) not in visited:
                        queue.append(newNode)
                        visited.append((x, y))
        return

    

                




