# https://www.codewars.com/kata/5270d0d18625160ada0000e4
# 2023-05-24T18:00:03.914+0000
def score(dice):
    # Array mutation is banned lol
    rolls = dice.copy()
    score = 0
    # Try and preferentially pick the highest scores
    while rolls.count(1) >= 3:
        score += 1000
        for i in range(3):
            rolls.pop(rolls.index(1))
            
    while rolls.count(6) >= 3:
        score += 600
        for i in range(3):
            rolls.pop(rolls.index(6))
            
    while rolls.count(5) >= 3:
        score += 500
        for i in range(3):
            rolls.pop(rolls.index(5))
            
    while rolls.count(4) >= 3:
        score += 400
        for i in range(3):
            rolls.pop(rolls.index(4))
            
    while rolls.count(3) >= 3:
        score += 300
        for i in range(3):
            rolls.pop(rolls.index(3))
            
    while rolls.count(2) >= 3:
        score += 200
        for i in range(3):
            rolls.pop(rolls.index(2))
            
    while rolls.count(1) > 0:
        score += 100
        rolls.pop(rolls.index(1))
        
    while rolls.count(5) > 0:
        score += 50
        rolls.pop(rolls.index(5))
        
    return score