class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        length = len(words[0])
        total = len(words)*length

        res = []
        word_count = {}
        
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        for i in range(length):
            left = i
            sub_count = {}
            count = 0

            for j in range(i,len(s)-length+1,length):
                sub_word = s[j:j+length]
                if sub_word in word_count:
                    if sub_word in sub_count:
                        sub_count[sub_word] += 1
                    else:
                        sub_count[sub_word] = 1
                    count += 1

                    while sub_count[sub_word]> word_count[sub_word]:
                        sub_count[s[left:left + length]] -= 1
                        count -= 1
                        left += length
                    if count == len(words):
                        res.append(left)
                else:
                    sub_count.clear()
                    count = 0
                    left = j+length
        return res
