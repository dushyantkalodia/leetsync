class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def create_subset(i):
            if (subset[:]) in res:
                return

            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            create_subset(i+1)

            subset.pop()
            create_subset(i+1)
        
        create_subset(0)
        return res