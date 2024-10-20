# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def solve(root,ans,level):
            if root is None:
                return

            if len(ans) == level:
                ans.append(root.val)
            solve(root.right,ans,level+1)
            solve(root.left,ans,level+1)

        solve(root,ans,0)
        return ans