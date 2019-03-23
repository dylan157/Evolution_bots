from MapPhysics import MapPhysics

class Botbuilder(object):
    def __init__(self, map):
        self.x = 0
        self.y = 0
        self.name = "Dude"
        self.age = 0
        self.hunger = 50
        self.memory = 16
        self.sight = 5
        self.dna = 2
        self.fertile = 50
        self.babys = 0
        self.last_move = "00"
        self.life = True
        self.targets = [map.chest_icon, map.death_icon, map.grass_icon, map.dirt_icon]
        self.avoid = ["x"]
    
