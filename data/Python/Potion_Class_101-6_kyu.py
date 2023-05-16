# https://www.codewars.com/kata/5981ff1daf72e8747d000091
# 2023-04-19T18:34:38.470+0000
import math

class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        total_volume = self.volume + other.volume
        new_color = [0, 0, 0]
        for i, col in enumerate(self.color):
            new_color[i] = math.ceil(self.color[i] * self.volume / total_volume + other.color[i] * other.volume / total_volume)
        
        return Potion(tuple(new_color), total_volume)