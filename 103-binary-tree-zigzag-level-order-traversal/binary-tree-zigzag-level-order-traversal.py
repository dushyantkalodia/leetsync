# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        
        leftToRIght = True
        q = deque([root])

        while q:
            n = len(q)
            data = [0]* n
            for i in range(n):
                temp = q.popleft()
                idx = i if leftToRIght else n-i-1
                data[idx] = temp.val

                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
            leftToRIght = not leftToRIght
            ans.append(data)
        return ans
