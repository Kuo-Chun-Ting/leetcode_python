from ...model import TreeNode
from .a2_iteration import Solution


def test_when_no_node_then_return_empty_list():
    # Arrange
    root = None

    # Act
    result = Solution().levelOrder(root)

    # Assert
    assert result == []


def test_when_1_level_then_return_expected_result():
    # Arrange
    root = TreeNode(val=1)

    # Act
    result = Solution().levelOrder(root)

    # Assert
    assert result == [[1]]


def test_when_2_levels_then_return_expected_result():
    # Arrange
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)

    # Act
    result = Solution().levelOrder(root)

    # Assert
    assert result == [[1], [2, 3]]


def test_when_3_levels_then_return_expected_result():
    # Arrange
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)
    root.left.left = TreeNode(val=4)

    # Act
    result = Solution().levelOrder(root)

    # Assert
    assert result == [[1], [2, 3], [4]]
