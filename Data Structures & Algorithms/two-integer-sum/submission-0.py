class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_hash = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_hash:
                return [diff_hash[diff], i]
            else:
                diff_hash[nums[i]] = i