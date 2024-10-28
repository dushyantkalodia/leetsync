class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i,j = 0,0
        minL = sys.maxsize
        sum = 0

        while j<n:
            sum += nums[j]
            while sum >= target:
                minL = min(minL,j-i+1)
                sum -= nums[i]
                i += 1
            j += 1
        return 0 if minL == sys.maxsize else minL