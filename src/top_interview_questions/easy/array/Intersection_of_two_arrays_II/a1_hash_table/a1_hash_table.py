class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection_dict: dict[int, int] = {}

        for n in nums1:
            if n not in intersection_dict:
                intersection_dict[n] = 0
            intersection_dict[n] += 1

        intersection_list: list[int] = []
        for n in nums2:
            if n in intersection_dict and intersection_dict[n] > 0:
                intersection_list.append(n)
                intersection_dict[n] -= 1

        return intersection_list
