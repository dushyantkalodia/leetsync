class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        last_idx = -1
        res = 0

        while j<len(nums):
            if nums[j]== 0:
                i = last_idx + 1
                last_idx = j
            res = max(res,j-i)
            j+=1
        return res
