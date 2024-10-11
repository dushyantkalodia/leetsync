class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapsT,maptS = {} , {}
        for i in range(len(s)):
            c1,c2 = s[i],t[i]
            
            if((c1 in mapsT and mapsT[c1] != c2) or (c2 in maptS and maptS[c2] != c1)):
                return False
            mapsT[c1] = c2
            maptS[c2] = c1
        return True
