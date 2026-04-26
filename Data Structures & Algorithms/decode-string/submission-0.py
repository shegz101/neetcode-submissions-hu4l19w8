class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        current_num = 0
        current_str = ""

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)

            elif ch == "[":
                stk.append((current_str, current_num))
                current_num = 0
                current_str = ""
            elif ch == "]":
                prev_str, curr_num = stk.pop()
                current_str = prev_str + current_str * curr_num
            else:
                current_str += ch
        return current_str