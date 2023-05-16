# https://www.codewars.com/kata/60f3639b539c06001a076267
# 2023-05-11T06:03:04.616+0000
from typing import Dict, List

import numpy as np
from numpy import linalg as LA


def get_greatest_spore_multiplier(graph: Dict[int, List[int]]) -> float:
    if graph == {}:
        return 0
    
    # Create the node graph in matrix format
    nodes = np.zeros((len(graph), len(graph)))
    # Go through the graph dictionary to fill it in
    for key, value in graph.items():
        # The key represents which row we're on
        # It also represents a -1 in the matrix
        nodes[key][key] = -1
        # Iterate over the value (which is a list)
        for node in value:
            nodes[key][node] = 1
            
    # Find the eigenvalues
    eigenvalues = np.linalg.eig(nodes)
    
    # Find the maximum eigenvalue
    # Remember to add 1 since Av = (a-1)v = lambdav => a = lambda + 1            
    return max(eigenvalues[0]) + 1