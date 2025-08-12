class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
            return

        if n == 0:
            return

        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 or j >= 0:
            if i < 0:
                nums1[: k + 1] = nums2[: j + 1]
                break

            if j < 0:
                nums1[: k + 1] = nums1[: i + 1]
                break

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
