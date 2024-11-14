class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        l = 1
        r = max(quantities)
        res = r
        
        def possible(x,quantities,shops):
            for product in quantities:
                shops -= (product + x - 1)//x
                if shops<0:
                    return False
            return True

        while l<=r:
            mid = l + (r-l)//2

            if possible(mid,quantities,n):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res