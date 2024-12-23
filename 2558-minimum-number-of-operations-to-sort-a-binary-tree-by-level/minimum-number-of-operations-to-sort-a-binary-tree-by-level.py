# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0
        def countMinSwapsToSort(vec):
            swaps = 0
            sortedVec = vec[:]
            sortedVec.sort()
            mp = {}
            for idx, val in enumerate(vec):
                mp[val] = idx
            
            for i in range(len(vec)):
                
                if vec[i] == sortedVec[i]:
                    continue
                currIdx = mp[sortedVec[i]]
                mp[vec[i]] = currIdx
                mp[sortedVec[i]] = i
                
                vec[i], vec[currIdx] = vec[currIdx], vec[i]
                swaps += 1
            return swaps 
        while q:
            n = len(q)
            vec = []
            for _ in range(n):
                temp = q.popleft()
                vec.append(temp.val)
                
                # Add children to the queue
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

            # Count minimum swaps for the current level
            res += countMinSwapsToSort(vec)

        return res