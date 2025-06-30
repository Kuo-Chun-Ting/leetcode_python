from dataclasses import dataclass
from typing import Optional

from ...model import TreeNode


@dataclass
class StackItem:
    depth: int
    node: TreeNode | None


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        root_item = StackItem(
            depth=1,
            node=root,
        )
        stack: list[StackItem] = [root_item]
        max_depth = 0

        while stack:
            item = stack.pop()
            if item.node:
                max_depth = max(max_depth, item.depth)
                stack.append(StackItem(depth=item.depth + 1, node=item.node.left))
                stack.append(StackItem(depth=item.depth + 1, node=item.node.right))

        return max_depth
