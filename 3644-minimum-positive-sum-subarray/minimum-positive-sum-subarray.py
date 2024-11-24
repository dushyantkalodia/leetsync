class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minval = inf
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += nums[j]
                if l <= j-i+1 <= r and s > 0:
                    minval = min(minval,s)
        return -1 if minval == inf else minval