from .a2_using_string_split_method import Solution


def test_when_example1_then_return_1():
    # Arrange
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]

    # Act
    result = Solution().numUniqueEmails(emails)

    # Assert
    assert result == 2


def test_when_example2_then_return_1():
    # Arrange
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]

    # Act
    result = Solution().numUniqueEmails(emails)

    # Assert
    assert result == 3
