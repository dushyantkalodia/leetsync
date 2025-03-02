class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        res = []
        
        for  id,val in nums1:
            mp[id] += val
        
        for id,val  in nums2:
            mp[id] += val
        
        for key in sorted(mp.keys()):
            res.append([key,mp[key]])
        return res