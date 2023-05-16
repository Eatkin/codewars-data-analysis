# https://www.codewars.com/kata/587136ba2eefcb92a9000027
2023-04-28T16:24:55.944+0000
class SnakesLadders():

    def __init__(self):
        # Create player objects
        self.player_1 = Player(1)
        self.player_2 = Player(2)
        
        self.turn = self.player_1
        
        
        # Create game board pointers in a dictionary
        # These are positions of the snakes and ladders that point to their desinations
        self.board_dict = {
            2: 38,
            7: 14,
            8: 31,
            15: 26,
            16: 6,
            21: 42,
            28: 84,
            36: 44,
            46: 25,
            49: 11,
            51: 67,
            62: 19,
            64: 60,
            71: 91,
            74: 53,
            78: 98,
            87: 94,
            89: 68,
            92: 88,
            95: 75,
            99: 80
        }
        

    def play(self, die1, die2):        
        # Basic move
        player_num = 1
        if self.turn == self.player_2:
            player_num = 2
        
        # Check if we've already finished the game
        if self.player_1.pos == 100 or self.player_2.pos == 100:
            return "Game over!"
        
        pos = self.turn.pos
        pos += die1 + die2
        
        
        # "Bounce back" if necessary
        if pos > 100:
            pos = 100 - pos % 100
            
        # Check for snakes/ladders
        if pos in self.board_dict:
            pos = self.board_dict[pos]
        
        # Update player object
        self.turn.pos = pos
        
        # Winning conditions
        if pos == 100:
            if player_num == 1:
                return "Player 1 Wins!"
            return "Player 2 Wins!"
        
        position_statement = f"Player {player_num} is on square {self.turn.pos}"
        
        # Switch turns unless we've rolled a double
        if die1 != die2:
            if player_num == 1:
                self.turn = self.player_2
            else:
                self.turn = self.player_1
                
        return position_statement
                
        
        
class Player():
    def __init__(self, player_num):
        self.player_num = player_num
        self.pos = 0