class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newStr = ''
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]

        left_pointer, right_pointer = 0, len(s) - 1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1
            while right_pointer > left_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1
            if s[left_pointer].lower()  != s[right_pointer].lower():
                return False
            left_pointer += 1
            right_pointer -= 1
        return True 