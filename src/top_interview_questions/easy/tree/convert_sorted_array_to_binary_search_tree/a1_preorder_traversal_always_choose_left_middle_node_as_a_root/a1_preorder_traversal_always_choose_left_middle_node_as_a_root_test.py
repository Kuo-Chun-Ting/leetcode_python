from ...model import TreeNode
from .a1_preorder_traversal_always_choose_left_middle_node_as_a_root import Solution


def test_when_no_node_then_return_none():
    # Arrange
    nums = []

    # Act
    result = Solution().sortedArrayToBST(nums)

    # Assert
    assert result is None


def test_when_one_level_then_return_one_node():
    # Arrange
    nums = [1]

    # Act
    result = Solution().sortedArrayToBST(nums)

    # Assert
    assert result and result.val == 1


def test_when_rwo_levels_then_return_expected_result():
    # Arrange
    nums = [1, 2, 3]

    # Act
    result = Solution().sortedArrayToBST(nums)

    # Assert
    assert result and result.val == 2
    assert result.left and result.left.val == 1
    assert result.right and result.right.val == 3
