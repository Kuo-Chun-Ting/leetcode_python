import math
from collections import deque
from dataclasses import dataclass
from typing import Optional

from ...model import TreeNode


@dataclass
class QueueItem:
    node: TreeNode | None
    lower_bound: float
    upper_bound: float


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue: deque[QueueItem] = deque(
            [QueueItem(node=root, lower_bound=-math.inf, upper_bound=math.inf)]
        )

        while queue:
            item = queue.popleft()
            if not item.node:
                continue

            node = item.node
            lower_bound = item.lower_bound
            upper_bound = item.upper_bound

            if node.val <= lower_bound or node.val >= upper_bound:
                return False

            queue.append(
                QueueItem(node=node.left, lower_bound=lower_bound, upper_bound=node.val)
            )
            queue.append(
                QueueItem(
                    node=node.right, lower_bound=node.val, upper_bound=upper_bound
                )
            )

        return True
