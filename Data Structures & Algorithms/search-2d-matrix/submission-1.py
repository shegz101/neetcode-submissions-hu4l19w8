class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check if the last elemnt in each array is greater than or smaller than the target
        # start searching from the middle row
        first_row, last_row = 0, len(matrix) - 1

        # helper binary search
        def binarySearch(arr, target):
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2

                if target < arr[mid]:
                    r = mid - 1
                elif target > arr[mid]:
                    l = mid + 1
                else:
                    return True
            
            return False

        while first_row <= last_row:
            mid_row = (first_row + last_row) // 2
            mid_len = len(matrix[mid_row])

            if target < matrix[mid_row][0]:
                last_row = mid_row - 1
            elif target > matrix[mid_row][mid_len - 1]:
                first_row = mid_row + 1
            else:
                # target = target
                return binarySearch(matrix[mid_row],target)
        
        return False
