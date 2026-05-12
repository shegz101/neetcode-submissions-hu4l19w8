class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_p, r_p = 0, len(nums) - 1
        k = k % len(nums)

        while l_p < r_p:
            nums[l_p], nums[r_p] = nums[r_p], nums[l_p]
            l_p += 1
            r_p -= 1
        

        l_p, r_p = 0, k - 1
        while l_p < r_p:
            nums[l_p], nums[r_p] = nums[r_p], nums[l_p]
            l_p += 1
            r_p -= 1
        
        l_p, r_p = k, len(nums) - 1
        while l_p < r_p:
            nums[l_p], nums[r_p] = nums[r_p], nums[l_p]
            l_p += 1
            r_p -= 1