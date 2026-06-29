class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = float('-inf') 

        l, r = 0, len(heights) - 1

        while l < r:
            cur_capacity = min(heights[l], heights[r]) * (r - l)
            output = max(cur_capacity, output)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return output