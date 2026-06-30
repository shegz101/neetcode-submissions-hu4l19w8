class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Using negative marking method
        n = len(nums)

        # loop through nums and chnage negative numbers to zero
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        

        # now mark numbers with negative marking
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 *(n + 1)

        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i
        
        return n + 1
                


