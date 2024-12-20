# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root,0))
        maxWidth = 0
        while q:
            l = q[0][1]
            r = q[-1][1]
            maxWidth = max(maxWidth,r-l+1)
            n = len(q)
            for _ in range(len(q)):
                curr,idx = q.popleft()
                if curr.left:
                    q.append((curr.left,2*idx+1))
                if curr.right:
                    q.append((curr.right,2*idx+2))

                
        return maxWidth
