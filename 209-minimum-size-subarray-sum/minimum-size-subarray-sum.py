class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0 
        j = 0
        sum = 0
        minl = sys.maxsize
        while j<n:
            sum += nums[j]
            while sum>=target:
                minl = min(minl,j-i+1)
                sum -= nums[i]
                i+= 1
            j += 1
        return 0 if minl == sys.maxsize else minl