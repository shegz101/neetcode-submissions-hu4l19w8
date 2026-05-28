class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = float('-inf')
        cur_count = 0

        for num in nums:
            if num == 1:
                cur_count += 1
            elif num == 0 and cur_count > 0:
                count = max(count, cur_count)
                cur_count = 0
        count = max(count, cur_count)
        
        return count