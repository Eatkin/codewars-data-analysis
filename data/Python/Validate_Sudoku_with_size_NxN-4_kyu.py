# https://www.codewars.com/kata/540afbe2dc9f615d5e000425
# 2023-04-24T09:57:50.421+0000
import numpy as np
import math

class Sudoku(object):

    def __init__(self, data):
        try:
            self.data = np.array(data)
            self.size = len(self.data)
            self.valid = True
            
            # Do some preliminary checks to check we're actually valid
            invalid_nums = set([x for x in self.data.flatten() if not isinstance(x, np.int64) or x>self.size or x<1])
            if invalid_nums:
                self.valid = False
            
        except ValueError:
            print("Invalid sudoku provided")
            self.valid = False
            

    def is_valid(self):
        if not self.valid:
            return False
        
        # Check successively each 3x3 section, each row, then each column
        # Do this all in one loop to avoid 3 loops
        section_size = int(math.sqrt(self.size))
        for i in range(self.size):
            # First slice the data into sections
            xx = (i % section_size) * section_size
            yy = (i // section_size) * section_size
            data_slice = self.data[xx:xx + section_size, yy:yy + section_size]
            # Check the length of the list of the members of the slice is equal to the set of the members of the slice
            if len(data_slice.flatten()) != len(set(data_slice.flatten())):
                self.valid = False
                return False

            # Now we'll check each row is valid - this is easy and requires no data transformation
            if len(self.data[i]) != len(set(self.data[i])):
                self.valid = False
                return False

            # Now check each column is valid
            data_slice = self.data[:, i]
            if len(data_slice.flatten()) != len(set(data_slice.flatten())):
                self.valid = False
                return False
            
        # If we pass all tests then the grid is valid
        return True