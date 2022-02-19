def costBenefit(self, map, player_info, tile):
    #Tile class members: 
    #x (int)
    #y (int)
    #passability (float) - the multiplicative cost of building on this tile
    #population (int) - number of people living on this tile
    #structure (Structure object) - structure built on this Tile, or None

    #check if we can build
    if map[tile.x][tile.y].structure is None:
        towerCost = StructureType.TOWER.get_base_cost() * map[tile.x][tile.y].passability
        roadCost = StructureType.ROAD.get_base_cost() * map[tile.x][tile.y].passability

        #population of current tile
        population = tile.population

        tileList = [(1, 0), (-1, 0), (0, 1), (0, -1),
                    (1, 1), (1, -1), (-1, -1), (-1, 1),
                    (2, 0), (-2, 0), (0, 2), (0, -2)]
        
        for dt in tileList:
            population += map[tile.x + dt[0]][tile.y + dt[1]].population

        # check if my team can afford this structure
        if player_info.money >= towerCost:
            q.pq_insert(tile.x, tile.y, "TOWER", population + (player_info.money/towerCost))
        if player_info.money >= roadCost:
            q.pq_insert(tile.x, tile.y, "ROAD", player_info.money/roadCost)
    
    return

