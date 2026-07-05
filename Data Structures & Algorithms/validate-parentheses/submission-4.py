class Solution:
    def isValid(self, s: str) -> bool:
        brackets_hash = {"(": ")", "[": "]", "{": "}"}
        stk = []

        for ch in s:
            if ch in "({[":
                stk.append(ch)
            elif stk and ch == brackets_hash[stk[-1]]:
                stk.pop()
            else:
                return False
        
        if len(stk) == 0:
            return True
        else:
            return False
