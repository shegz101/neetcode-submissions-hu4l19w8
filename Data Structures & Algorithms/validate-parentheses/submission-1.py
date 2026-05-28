class Solution:
    def isValid(self, s: str) -> bool:
        track_brackets = {")": "(", "]": "[", "}": "{"}

        stk = []

        for ch in s:
            if ch in "({[":
                stk.append(ch)
            else:
                if stk and track_brackets[ch] == stk[-1]:
                    stk.pop()
                else:
                    return False
        
        return True if len(stk) == 0 else False

