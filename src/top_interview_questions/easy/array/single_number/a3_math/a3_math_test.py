from .a3_math import Solution


def test_when_one_num_then_return_itself():
    # Arrange
    nums = [1]

    # Act
    result = Solution().singleNumber(nums)

    # Assert
    assert result == 1


def test_when_normal_case_then_return_expected_result():
    # Arrange
    nums = [1, 1, 2, 5, 2, 5, 6]

    # Act
    result = Solution().singleNumber(nums)

    # Assert
    assert result == 6
