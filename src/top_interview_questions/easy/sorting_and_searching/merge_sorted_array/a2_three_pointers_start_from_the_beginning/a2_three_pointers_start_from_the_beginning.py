class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1_copy = nums1[:m]
        i, j, k = 0, 0, 0

        while i < m or j < n:
            if i == m:
                nums1[k:] = nums2[j:]
                break

            if j == n:
                nums1[k:] = nums1_copy[i:]
                break

            if nums1_copy[i] < nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k += 1
