class Solution:
    # helper function to check max
    def findMaxInSubarray(self, subarr: List[int]) -> int:
        max_ele = float('-inf')

        for i in range(len(subarr)):
            max_ele = max(max_ele, subarr[i])
        
        return max_ele


    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i != len(arr) - 1:
                max_ele = self.findMaxInSubarray(arr[i + 1:])
                arr[i] = max_ele
            else:
                arr[len(arr) - 1] = -1
        
        return arr
       
    


    
