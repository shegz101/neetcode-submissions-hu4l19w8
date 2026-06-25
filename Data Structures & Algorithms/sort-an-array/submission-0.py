class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left_subarr = arr[L:M+1]
            right_subarr = arr[M+1:R+1]

            # define pointer for arr, left & righ subarr
            i, l, r = L, 0, 0

            while l < len(left_subarr) and r < len(right_subarr):
                if left_subarr[l] <= right_subarr[r]:
                    arr[i] = left_subarr[l]
                    l += 1
                else:
                    arr[i] = right_subarr[r]
                    r += 1 
                i += 1
            
            while l < len(left_subarr):
                arr[i] = left_subarr[l]
                l += 1
                i += 1
            

            while r < len(right_subarr):
                arr[i] = right_subarr[r]
                r += 1
                i += 1
            


        def mergeSort(arr, l, r):
            # base case
            if l == r:
                return
            
            # get middle of array so you can divide it
            m = (l + r) // 2

            # mergesort on the left part that we got after dividing
            mergeSort(arr, l, m)
            # mergesort on the right part that we got after dividing
            mergeSort(arr, m + 1, r)
            # merge it after
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)

        return nums
