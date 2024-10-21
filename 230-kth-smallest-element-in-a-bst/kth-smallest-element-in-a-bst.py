# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root,values):
            if root is None:
                return
            inOrder(root.left,values)
            values.append(root.val)
            inOrder(root.right,values)
        values = []
        inOrder(root,values)
        if 1 <= k <= len(values):
            return values[k - 1]  # Return the k-th smallest element
        else:
            return None 