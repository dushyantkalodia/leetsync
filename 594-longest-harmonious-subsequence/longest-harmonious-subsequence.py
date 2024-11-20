class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        i = 0
        j = 0
        n = len(nums)
        maxLen = 0
        while j<n:
            diff = nums[j] - nums[i]
            if diff == 1:
                maxLen = max(maxLen,j-i+1)
                j+=1
            elif diff == 0:
                j+=1
            else:
                i+=1
        return maxLen