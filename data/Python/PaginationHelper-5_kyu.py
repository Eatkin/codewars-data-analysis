# https://www.codewars.com/kata/515bb423de843ea99400000a
# 2023-04-26T17:52:42.325+0000
# TODO: complete this class

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    
    return 0

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        pass

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
        pass

    # returns the number of pages
    def page_count(self):
        return self.item_count() // self.items_per_page + sign(self.item_count() % self.items_per_page)
        pass

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        range = self.page_count()
        
        # Out of range
        if page_index >= range or page_index < 0:
            return -1
        
        # Only one page
        if range == 1:
            return self.item_count()
        
        # Any page that's not the last
        if page_index < range - 1:
            return self.items_per_page
        
        # Final page for a book that has multiple pages
        return self.item_count() % self.items_per_page

        pass

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        range = self.item_count()
        if item_index < 0 or item_index >= range:
            return -1
        
        return item_index // self.items_per_page
        pass
