class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        length = 0
        n = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in dic and dic[ch]>=n:
                n = dic[ch] + 1
            else:
                length = max(length,i-n+1)
            dic[ch] = i
        return length            

        
