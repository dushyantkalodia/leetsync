class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        j = 0
        count = {'a': 0, 'b': 0, 'c': 0}
        notdeleteWindowSize = 0
        for ch in s:
            count[ch] += 1
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1
        for j in range(n):
            count[s[j]] -= 1
            while count['a'] < k or count['b'] < k or count['c'] < k:
                count[s[i]] += 1    
                i += 1
            notdeleteWindowSize = max(notdeleteWindowSize,j-i+1)
            
        return n - notdeleteWindowSize
            