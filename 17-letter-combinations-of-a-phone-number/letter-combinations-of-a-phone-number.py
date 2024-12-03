class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        res = []
        mp = {
            '2': "abc", '3': "def", '4': "ghi",
            '5': "jkl", '6': "mno", '7': "pqrs",
            '8': "tuv", '9': "wxyz"
        }

        def solve(idx: int, digits: str, temp: str):
            if idx == len(digits):
                res.append(temp)  # Add the combination to the result
                return
            
            ch = digits[idx]
            strr = mp[ch]
            
            for char in strr:
                solve(idx + 1, digits, temp + char)  # Concatenate character to temp

        solve(0, digits, "")
        return res