
class Solution:
    def solve(self, nums: List[int], idx: int, k: int, mp: defaultdict) -> int:
        if idx == len(nums):
            return 1

        taken = 0
        if mp[nums[idx] - k] == 0 and mp[nums[idx] + k] == 0:
            mp[nums[idx]] += 1
            taken = self.solve(nums,idx+1,k,mp)
            mp[nums[idx]] -= 1
        
        notTaken = self.solve(nums,idx+1,k,mp)

        return taken + notTaken

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        res = self.solve(nums,0,k,mp)
        return res - 1