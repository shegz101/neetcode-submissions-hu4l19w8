class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_tracker = [0] * 26

        for ch in s:
            ch_tracker[ord(ch) - ord('a')] += 1
        
        for i, ch in enumerate(s):
            if ch_tracker[ord(ch) - ord('a')] == 1:
                return i
        
        return -1