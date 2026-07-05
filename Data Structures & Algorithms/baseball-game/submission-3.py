class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        total = 0

        for ch in operations:
            if ch == "C":
                stk.pop()
            elif ch == "+":
                a = stk[-1]
                b = stk[-2]
                c = a + b
                stk.append(c)
            elif ch == "D":
                a = stk[-1]
                stk.append(2 * a)
            else:
                stk.append(int(ch))
        
        while stk:
            total += stk.pop()
        
        return total
            