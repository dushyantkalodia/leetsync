class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        m = len(queries)

        cumSum = [0]*n
        #cumSum[i] = total count of violating indices till index i
        cumSum[0] = 0
        for i in range(1,n):
            if nums[i]%2 == nums[i-1]%2:
                cumSum[i] = cumSum[i-1]+1
            else:
                cumSum[i] = cumSum[i-1] 
        res = [False]*m
        i = 0
        for q in queries:
            start = q[0]
            end = q[1]

            if cumSum[end] - cumSum[start] == 0:
                res[i] = True
            i+=1
        return res