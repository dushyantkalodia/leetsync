class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        memo = {}
        n = len(words)
        st = set(words)
        res = []

        def isConcatenated(word,st):
            if word in memo:
                return memo[word]
            

            l  = len(word)
            for i in range(l):
                prefix = word[0:i+1]
                suffix = word[i+1:]

                if (prefix in st and (isConcatenated(suffix, st) or suffix in st)):
                    memo[word] = True
                    return True
            
            memo[word] = False
            return False


        for i in range(n):
            word = words[i]
            if isConcatenated(word,st):
                res.append(word)
        return res
