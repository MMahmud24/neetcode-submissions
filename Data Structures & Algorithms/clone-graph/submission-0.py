"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}

        def dfs(orig):
            if orig in clones:
                return clones[orig]
            copy = Node(orig.val)
            clones[orig] = copy          
            for nei in orig.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)

        


        