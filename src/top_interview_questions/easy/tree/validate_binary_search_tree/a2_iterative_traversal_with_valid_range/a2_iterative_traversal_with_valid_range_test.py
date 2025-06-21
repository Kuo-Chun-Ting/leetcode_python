from ...model import TreeNode
from .a2_iterative_traversal_with_valid_range import Solution


def test_when_1_level_tree_then_return_true():
    # Arrange
    root = TreeNode(val=1)

    # Act
    result = Solution().isValidBST(root)

    # Assert
    assert result is True


def test_when_2_level_valid_tree_then_return_true():
    # Arrange
    root = TreeNode(val=2)
    root.left = TreeNode(val=1)

    # Act
    result = Solution().isValidBST(root)

    # Assert
    assert result is True


def test_when_2_level_invalid_tree_then_return_false():
    # Arrange
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)

    # Act
    result = Solution().isValidBST(root)

    # Assert
    assert result is False


def test_when_3_level_valid_tree_then_return_true():
    # Arrange
    root = TreeNode(val=5)
    root.left = TreeNode(val=1)
    root.left.right = TreeNode(val=3)

    # Act
    result = Solution().isValidBST(root)

    # Assert
    assert result is True


def test_when_3_level_invalid_tree_then_return_false():
    # Arrange
    root = TreeNode(val=5)
    root.left = TreeNode(val=1)
    root.left.right = TreeNode(val=6)

    # Act
    result = Solution().isValidBST(root)

    # Assert
    assert result is False


def test_when_same_value_then_return_false():
    # Arrange
    root = TreeNode(val=2)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=2)

    # Act
    result = Solution().isValidBST(root)

    # Assert
    assert result is False
