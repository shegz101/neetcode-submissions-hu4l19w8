class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # reverse iteration, each max will basically be the old max for the previous element and the value of the previous element from the original array
        n = len(arr)
        res = [0] * n

        curr_max = -1

        for i in range(n - 1, -1, -1):
            res[i] = curr_max
            curr_max = max(curr_max, arr[i])
        
        return res