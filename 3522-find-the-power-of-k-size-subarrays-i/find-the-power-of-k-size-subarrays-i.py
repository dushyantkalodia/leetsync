class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n<k:
            return [-1]*(n-k+1)
        res = [-1]*(n-k+1)
        count = 1

        for i in range(1,k):
            if nums[i] == nums[i-1]+1:
                count += 1
            else:
                count = 1
        if count == k:
            res[0] = nums[k - 1]
        i = 1
        j = k

        while j<n:
            if nums[j] == nums[j-1]+1:
                count += 1
            else:
                count = 1
            if count>=k:
                res[i] = nums[j]
            i+=1
            j+=1
        return res
