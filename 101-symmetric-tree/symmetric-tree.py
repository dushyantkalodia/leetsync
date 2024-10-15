# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,l,r)->bool:
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        if l.val == r.val and self.check(l.left,r.right) and self.check(l.right,r.left):
            return True
        return False




    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.check(root.left,root.right)