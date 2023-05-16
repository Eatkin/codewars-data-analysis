# https://www.codewars.com/kata/568dcc3c7f12767a62000038
2023-05-12T09:42:11.505+0000
class Person:
    def __init__(self, name, employed, vacation):
        self.employed = employed
        self.vacation = vacation
        self.name = name
        
    def is_employed(self):
        return self.employed
    
    def is_on_vacation(self):
        return self.vacation
    
def set_alarm(employed, vacation):
    Geoffrey = Person("Geoffrey", employed, vacation)
    return Geoffrey.is_employed() and not Geoffrey.is_on_vacation()