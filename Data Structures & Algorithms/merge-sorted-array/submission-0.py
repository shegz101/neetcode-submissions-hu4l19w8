class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_p = m - 1
        nums2_p = n - 1
        last_num = m + n - 1

        while nums2_p >= 0:
            if nums1_p >= 0 and nums1[nums1_p] > nums2[nums2_p]:
                nums1[last_num] = nums1[nums1_p]
                nums1_p -= 1
            else:
                nums1[last_num] = nums2[nums2_p]
                nums2_p -= 1
            last_num -= 1
