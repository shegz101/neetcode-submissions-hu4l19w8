class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1p = m - 1
        nums2p = n - 1
        last_nump = m + n - 1

        while nums2p >= 0:
            if nums1p >= 0 and nums1[nums1p] > nums2[nums2p]:
                nums1[last_nump] = nums1[nums1p]
                nums1p -= 1
            else:
                nums1[last_nump] = nums2[nums2p]
                nums2p -= 1
            last_nump -= 1
