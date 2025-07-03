from ...model import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def helper(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            p = (left + right) // 2
            root = TreeNode(val=nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)
