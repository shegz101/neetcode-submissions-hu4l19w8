class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for ch in operations:
            if ch.lstrip('-').isdigit():
                stk.append(int(ch))
            elif ch == "+":
                stk.append(stk[-1] + stk[-2])
            elif ch == "C":
                stk.pop()
            else:
                stk.append(2 * stk[-1])
        
        return sum(stk)