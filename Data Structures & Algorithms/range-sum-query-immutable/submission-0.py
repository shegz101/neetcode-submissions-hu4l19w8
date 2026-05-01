class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixArray = []
        start = 0
        for i in range(len(nums)):
            if i == start:
                self.prefixArray.append(nums[i])
            else:
                self.prefixArray.append(self.prefixArray[i - 1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixArray[right]
        else:
            return self.prefixArray[right] - self.prefixArray[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)