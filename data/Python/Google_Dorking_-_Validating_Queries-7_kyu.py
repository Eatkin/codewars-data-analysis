# https://www.codewars.com/kata/62cb487e43b37a5829ab5752
# 2023-05-08T13:00:37.229+0000
from preloaded import FILTERS
import re

def is_valid(query: str) -> bool:
    filters = re.findall(r"(\b\w+):", query)
    for filter in filters:
        if not filter in FILTERS:
            return False
        
    return True
