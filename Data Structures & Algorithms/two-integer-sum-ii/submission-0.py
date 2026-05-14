class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_p, r_p = 0, len(numbers) -1

        while l_p < r_p:
            curSum = numbers[l_p] + numbers[r_p]
            if curSum > target:
                r_p -= 1
            elif curSum < target:
                l_p += 1
            else:
                return [l_p + 1, r_p + 1]
        
        return []