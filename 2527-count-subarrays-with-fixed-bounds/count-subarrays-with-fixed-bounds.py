class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        n = len(nums)
        minkPosition = -1
        maxkPosition = -1
        culpritInd = -1

        for i in range(n):
            if nums[i]<minK or nums[i] > maxK:
                culpritInd = i
            if nums[i] == minK:
                minkPosition = i
            if nums[i] == maxK:
                maxkPosition = i
            smaller = min(minkPosition,maxkPosition)
            temp = smaller - culpritInd
            res += 0 if temp<=0 else temp
        return res