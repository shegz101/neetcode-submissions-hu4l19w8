class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = 2 * n

        ans = [0] * m

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans
    