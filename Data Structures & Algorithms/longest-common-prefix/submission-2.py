class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""

        for i in range(len(strs[0])):
            curr_ele = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != curr_ele:
                    return output
            output += curr_ele
        
        return output