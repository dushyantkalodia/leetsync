class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = [0] * 26
        for i in s: count[ord(i) - ord('a')] += 1 

        first_largest = 25
        res = ""
        while first_largest >= 0: 
            if count[first_largest] <= repeatLimit: 
                res += chr(first_largest + 97) * count[first_largest] 
                first_largest -= 1 
            else:
                #search for the second largest char
                res += chr(first_largest + 97) * repeatLimit
                count[first_largest] -= repeatLimit 
                second_largest = first_largest - 1 
                found = False
                while second_largest >= 0: 
                    if count[second_largest] > 0: 
                        count[second_largest] -= 1
                        res += chr(second_largest + 97)
                        found = True 
                        break
                    second_largest -= 1  
                if not found: return res
        return res