from ...model import TreeNode
from .a2_iterative import Solution


def test_when_1_level_tree_then_return_true():
    # Arrange
    root = TreeNode(val=1)

    # Act
    result = Solution().isSymmetric(root)

    # Assert
    assert result is True


def test_when_2_level_valid_tree_then_return_true():
    # Arrange
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=2)

    # Act
    result = Solution().isSymmetric(root)

    # Assert
    assert result is True


def test_when_2_level_invalid_tree_then_return_false():
    # Arrange
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)

    # Act
    result = Solution().isSymmetric(root)

    # Assert
    assert result is False


def test_when_valid_tree_with_null_node_then_return_true():
    # Arrange
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=2)
    root.left.left = None
    root.left.right = TreeNode(val=3)
    root.right.left = TreeNode(val=3)
    root.right.right = None

    # Act
    result = Solution().isSymmetric(root)

    # Assert
    assert result is True
