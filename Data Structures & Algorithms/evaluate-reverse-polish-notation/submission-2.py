class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for ch in tokens:
            if ch == "+":
                temp2 = stk.pop()
                temp1 = stk.pop()
                stk.append(temp1 + temp2)
            elif ch == "-":
                temp2 = stk.pop()
                temp1 = stk.pop()
                stk.append(temp1 - temp2)
            elif ch == "*":
                temp2 = stk.pop()
                temp1 = stk.pop()
                stk.append(temp1 * temp2)
            elif ch == "/":
                temp2 = stk.pop()
                temp1 = stk.pop()
                stk.append(int(temp1 / temp2))
            else:
                stk.append(int(ch))

        return stk[-1]