class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(curr,pos,target):
            if target == 0:
                res.append(curr[:])
                return
            prev = -1
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                if candidates[i]>target:
                    break
                curr.append(candidates[i])
                dfs(curr,i,target-candidates[i])
                curr.pop()
                prev = candidates[i]
                
        dfs([],0,target)
        return res