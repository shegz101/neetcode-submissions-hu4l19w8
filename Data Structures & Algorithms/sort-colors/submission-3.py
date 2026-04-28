class Solution: 
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer, one_pointer = 0, 0
        two_pointer = len(nums) - 1

        def swap(left, right):
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp 

        while one_pointer <= two_pointer:
            if nums[one_pointer] == 0:
                swap(zero_pointer, one_pointer)
                zero_pointer += 1
                one_pointer += 1
            elif nums[one_pointer] == 1:
                one_pointer += 1
            elif nums[one_pointer] == 2:
                swap(one_pointer, two_pointer)
                two_pointer -= 1
        return nums
