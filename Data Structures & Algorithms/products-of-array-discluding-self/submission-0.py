class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefix_arr = [0] * len(nums)
        suffix_arr = [0] * len(nums)
        i = 0
        j = len(nums) - 1

        while i < len(nums):
            if i == 0:
                prefix_arr[0] = 1
            else:
                prefix_arr[i] = prefix_arr[i - 1] * nums[i - 1]
            i += 1
                
        while j >= 0:
            if j == len(nums) - 1:
                suffix_arr[j] = 1
            else:
                suffix_arr[j] = suffix_arr[j + 1] * nums[j + 1]
            j -= 1
        
        for i in range(len(nums)):
            output[i] = prefix_arr[i] * suffix_arr[i]
        
        return output

