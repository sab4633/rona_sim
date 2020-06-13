import random


class Blob:
    cur_local = -1;
    infection_chance = .3
    max_locations = 3
    visited = 0
    #infected = False;

    def __init__(self):
        self.infected = False

    def infect(self, other_Blob):
        if self.infected:
            rando = random.randInt(0,1)
            if(rando<=self.infection_chance):
                other_Blob.infected = True







