# https://www.codewars.com/kata/58bee820e9f98b215200007c
# 2023-06-05T16:04:17.475+0000
import re
def select(memory):
    pattern = re.compile(r'!([\w-]+ [\w-]+),? ?([\w-]+ [\w-]+)?,?')
    matches = re.findall(pattern, memory)
    if matches == []:
        return memory
    
    hated_people = []
    for match in matches:
        for i in range(2):
            if match[i] != '':
                hated_people.append(match[i])
    
    memory = [memory for memory in memory.split(", ") if "!" not in memory and not any(person in memory for person in hated_people)]
    return ", ".join(memory)
    