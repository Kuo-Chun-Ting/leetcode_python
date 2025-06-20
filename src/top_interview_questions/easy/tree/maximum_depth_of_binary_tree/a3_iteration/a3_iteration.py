from dataclasses import dataclass
from typing import Optional

from ...model import TreeNode


@dataclass
class QueueItem:
    depth: int
    node: TreeNode | None


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        root_item = QueueItem(
            depth=1,
            node=root,
        )
        queue: list[QueueItem] = [root_item]
        max_depth = 0

        while queue:
            item = queue.pop()
            if item.node:
                max_depth = max(max_depth, item.depth)
                queue.append(QueueItem(depth=item.depth + 1, node=item.node.left))
                queue.append(QueueItem(depth=item.depth + 1, node=item.node.right))

        return max_depth
