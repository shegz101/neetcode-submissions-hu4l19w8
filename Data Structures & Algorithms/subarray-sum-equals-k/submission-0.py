class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        currSum = 0
        output = 0

        for num in nums:
            currSum += num 
            if currSum - k in prefixSum:
                output += prefixSum[currSum - k]
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
            # if currSum in prefixSum:
            #     prefixSum[currSum] += 1
            # else:
            #     prefixSum[currSum] = 1
        
        return output 