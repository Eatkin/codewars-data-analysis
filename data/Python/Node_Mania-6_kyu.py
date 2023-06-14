# https://www.codewars.com/kata/5567e7d0adb11174c50000a7
# 2023-06-07T09:01:55.395+0000
from preloaded import Node

def search_k_from_end(linked_list : Node, k : int):
    # We can get the length of the list in this jank-ass way
    list_length = str(linked_list).count("->") + 1
    
    # Trivial - k is larger than list length
    if k > list_length:
        return None
    
    # Loop until we find the target node
    elem = 0
    target = list_length - k
    node = linked_list.data
    while elem < target:
        linked_list = linked_list.next
        node = linked_list.data
        elem += 1

    return node