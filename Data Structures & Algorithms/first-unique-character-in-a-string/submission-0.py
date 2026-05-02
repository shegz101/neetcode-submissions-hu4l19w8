class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_tracker = {}

        for ch in s:
            if ch not in ch_tracker:
                ch_tracker[ch] = 1
            else:
                ch_tracker[ch] += 1
        

        for i, ch in enumerate(s):
            if ch_tracker[ch] == 1:
                return i
        
        return -1