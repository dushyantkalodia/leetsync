class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        curr = []
        

        def ispalindrome(s,l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(s,idx,curr,res):
            if idx == n:
                res.append(curr[:])
                return
        
            for i in range(idx,n):
                if ispalindrome(s,idx,i):
                    curr.append(s[idx:i + 1])
                    backtrack(s,i+1,curr,res)
                    curr.pop()
        backtrack(s,0,curr,res) 
        return res