# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            else:
                return max(height(root.left),height(root.right))+1
        if root is None:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        diff = abs(height(root.left) - height(root.right)) <= 1
        if left and right and diff:
            return True
        else:
            return False