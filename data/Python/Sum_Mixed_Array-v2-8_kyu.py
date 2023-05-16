# https://www.codewars.com/kata/57eaeb9578748ff92a000009
2023-05-07T08:40:03.115+0000
class list_of_numbers:
    def __init__(self, num_list):
        self.my_nums = num_list
        
    def get_num(self, index):
        if not self.is_integer(index):
            if self.is_string(index):
                self.convert_to_integer(index)
            else:
                return None
        return self.my_nums[index]
    
    def is_integer(self, index):
        return type(self.my_nums[index]) == int
    
    def is_string(self, index):
        return type(self.my_nums[index]) == str
    
    def convert_to_integer(self, index):
        self.my_nums[index] = int(self.my_nums[index])
        
    def get_length(self):
        return len(self.my_nums)

def sum_mix(arr):
    my_list = list_of_numbers(arr)
    sum = 0
    for i in range(my_list.get_length()):
        sum += my_list.get_num(i)
    
    return sum
    