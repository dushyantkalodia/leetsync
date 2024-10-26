"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = collections.deque()

        if root is not None:
            q.append((root,0))
        
        while len(q)>0:
            node,currentlevel = q.popleft()

            if len(q)>0:
                nextNode,nextNodeLevel = q[0]

                if currentlevel == nextNodeLevel:
                    node.next = nextNode
            for nextNode in [node.left,node.right]:
                if nextNode is not None:
                    q.append((nextNode,currentlevel + 1))   
        return root   