# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def solve(root):
            nonlocal maxSum
            if root is None:
                return 0
            l = solve(root.left)
            r = solve(root.right)
            
            niche_hi_mil_gya = l+r+root.val 

            koi_ek_acha = max(l,r)+root.val

            only_root_acha = root.val
            maxSum = max(maxSum,niche_hi_mil_gya,koi_ek_acha,only_root_acha)

            return  max(koi_ek_acha,only_root_acha)
        solve(root)
        return maxSum

            