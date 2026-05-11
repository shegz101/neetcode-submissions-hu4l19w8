class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""

        l_p = 0
        r_p = max(len(word1), len(word2))

        while l_p < r_p:
            if l_p < len(word1):
                new_string += word1[l_p]
            if l_p < len(word2):
                new_string += word2[l_p]
            l_p += 1
        
        return new_string