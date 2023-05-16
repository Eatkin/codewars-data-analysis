# https://www.codewars.com/kata/55a144eff5124e546400005a
2023-04-19T18:07:51.568+0000
class Person(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"