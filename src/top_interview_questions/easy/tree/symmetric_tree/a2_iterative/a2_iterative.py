from ...model import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        left_stack: list[TreeNode | None] = [root]
        right_stack: list[TreeNode | None] = [root]

        while left_stack or right_stack:
            left_node = left_stack.pop()
            right_node = right_stack.pop()

            if left_node is None and right_node is None:
                continue

            if left_node is None or right_node is None:
                return False

            if left_node.val != right_node.val:
                return False

            left_stack.append(left_node.left)
            left_stack.append(left_node.right)

            right_stack.append(right_node.right)
            right_stack.append(right_node.left)

        return True
