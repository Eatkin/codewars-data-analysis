# https://www.codewars.com/kata/51fda2d95d6efda45e00004e
# 2023-05-22T20:53:51.940+0000
# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method
ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        
    def inc_progress(self, rank):
        rank_pos = ranks.index(self.rank)
        challenge_rank_pos = ranks.index(rank)
        diff = challenge_rank_pos - rank_pos
        progress = 0
        if diff == -1:
            progress = 1
        elif diff == 0:
            progress = 3
        elif diff > 0:
            progress = 10 * diff * diff
            
        self.progress += progress
        
        while self.progress >= 100:
            try:
                self.rank = ranks[ranks.index(self.rank) + 1]
                self.progress -= 100
            except:
                self.rank = ranks[len(ranks) - 1]
                self.progress = 0
                break
                
        if self.rank == 8:
            self.progress = 0