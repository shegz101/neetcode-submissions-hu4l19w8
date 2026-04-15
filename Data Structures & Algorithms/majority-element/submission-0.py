from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       ele_count = Counter(nums)
       ele_tracker = len(nums) // 2


       for num, count in ele_count.items():
        if count >  ele_tracker:
            return num
      

