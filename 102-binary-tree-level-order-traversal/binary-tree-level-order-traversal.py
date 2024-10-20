# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque([root])
        if root is None:
            return ans
        while q:
            n = len(q)
            if n == 0:
                return ans
            
            data = []
            for _ in range(n):
                temp = q.popleft()
                data.append(temp.val)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
                
            ans.append(data)
        return ans