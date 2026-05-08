class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        output = 0

        for num in num_set:
            if (num - 1) not in num_set:
                curr_len = 1
                while (num + curr_len) in num_set:
                    curr_len += 1
                output = max(output, curr_len)
            
        return output 
            

        