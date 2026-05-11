class Solution:
    def validPalindrome(self, s: str) -> bool:
        l_p, r_p = 0, len(s) - 1

        # Helper function
        def isSubStringPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True 

        while l_p < r_p:
            if s[l_p] != s[r_p]:
                return isSubStringPalindrome(l_p + 1, r_p) or isSubStringPalindrome(l_p, r_p -1)
            l_p += 1
            r_p -= 1
        
        return True
            