"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        mp = {}
        q = deque([node])
        mp[node] = Node(node.val)
        while q:
            h = q.popleft()
            for neighbor in h.neighbors:
                if neighbor not in mp:
                    mp[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                mp[h].neighbors.append(mp[neighbor])
        return mp[node]
