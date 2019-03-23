from random import randint

class MapPhysics(object):

    def __init__(self, Map_Size_X, Map_Size_X_Y):


        self.Map_Size_X = Map_Size_X
        self.Map_Size_X_Y = Map_Size_X_Y

        self.object_board = []
        self.memory_board = []
        self.playerboard = []
        self.used_xy = []

        self.grass_icon = '"'
        self.dirt_icon = ' '
        self.death_icon = "X"
        self.chest_icon = "$"

        self.living_bots = []
        self.dead_bots = []

        self.time = 0






        for click in range(Map_Size_X_Y): #Map creator
            self.object_board.append([self.dirt_icon] * Map_Size_X) # Dirt placer
            self.playerboard.append([self.dirt_icon] * Map_Size_X) # Grass placer
            self.memory_board.append([0] * Map_Size_X)


    def print_board(self, board):
        for row in board:
            print "  ".join(row)
            print ""


    def Object_Placement(self, amount_to_place, icon_to_place, map):

        for items in range(amount_to_place):
            place_found = False
            overflow = 0
            if overflow > 10: break
            while not place_found:

                if overflow > 2: break

                place_x, place_z = randint(0, (self.Map_Size_X_Y-1)), randint(0, (self.Map_Size_X)-1)   
               
                if (str(place_x) + str(place_z)) in self.used_xy:
                    overflow += 1
                    pass

                else:

                    map[place_x][place_z] = icon_to_place
                    if map == self.object_board:
                        self.used_xy.append(str(place_x) + str(place_z))
                        self.memory_board[place_x][place_z] = 0
                    place_found = True
            else:pass

    def tidy(self):
        for bot in self.living_bots: # Make current posistion object icon + po sistion count += 1
            self.playerboard[bot.x][bot.y] = self.object_board[bot.x][bot.y] # Make bots current posision == object

    def nature(self):
        if self.time % 15 == 0: 
            self.Object_Placement(25, self.grass_icon, self.playerboard) #place grass

        if self.time % 100 == 0: 
            self.Object_Placement(1, self.chest_icon, self.object_board) #place chest





