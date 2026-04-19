class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        closeOpenBrackets = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeOpenBrackets:
                if stk and stk[-1] == closeOpenBrackets[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        return True if not stk else False