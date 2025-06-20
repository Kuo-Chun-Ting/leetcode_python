from ...model import TreeNode
from .a3_iteration import Solution


def test_when_no_node_then_return_0():
    # Arrange
    root = None

    # Act
    result = Solution().maxDepth(root)

    # Assert
    assert result == 0


def test_when_1_level_then_return_1():
    # Arrange
    root = TreeNode(val=1)

    # Act
    result = Solution().maxDepth(root)

    # Assert
    assert result == 1


def test_when_2_levels_then_return_2():
    # Arrange
    root = TreeNode(val=1)
    root.left = TreeNode(val=1)

    # Act
    result = Solution().maxDepth(root)

    # Assert
    assert result == 2


def test_when_3_levels_then_return_3():
    # Arrange
    # Arrange
    root = TreeNode(val=1)
    root.left = TreeNode(val=1)
    root.left.right = TreeNode(val=1)

    # Act
    result = Solution().maxDepth(root)

    # Assert
    assert result == 3
