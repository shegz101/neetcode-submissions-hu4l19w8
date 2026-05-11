class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_p = 1

        for r_p in range(1, len(nums)):
            if nums[r_p] != nums[r_p - 1]:
                nums[l_p] = nums[r_p]
                l_p += 1
        
        return l_p