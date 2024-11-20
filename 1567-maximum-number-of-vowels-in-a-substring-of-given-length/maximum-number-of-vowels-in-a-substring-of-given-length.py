class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = 0
        n = len(s)
        maxV = 0
        count = 0
        def isVowel(ch):
            return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

        while j<n:
            if isVowel(s[j]):
                count += 1
            if j-i+1 == k:
                maxV = max(maxV,count)
                if isVowel(s[i]):
                    count -= 1
                i += 1
            j += 1
        return maxV