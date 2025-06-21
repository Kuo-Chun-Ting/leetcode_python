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
        queue: list[StackItem] = [root_item]
        max_depth = 0

        while queue:
            item = queue.pop()
            if item.node:
                max_depth = max(max_depth, item.depth)
                queue.append(StackItem(depth=item.depth + 1, node=item.node.left))
                queue.append(StackItem(depth=item.depth + 1, node=item.node.right))

        return max_depth
