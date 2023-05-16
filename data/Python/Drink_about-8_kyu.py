# https://www.codewars.com/kata/56170e844da7c6f647000063
# 2023-05-14T20:44:52.494+0000
def people_with_age_drink(age):
    ages = [14, 18, 21, 500000]
    drinks = ["toddy", "coke", "beer", "whisky"]
    for tuple in zip(ages, drinks):
        if age < tuple[0]:
            return f"drink {tuple[1]}"
        
    return "You are dead"