# https://www.codewars.com/kata/55a144eff5124e546400005a
2023-04-19T18:05:18.795+0000
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"
        
    def getInfo(self):
        return self.indo