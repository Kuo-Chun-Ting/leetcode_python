from .a1_priority_queues import Solution


def test_when_example1_then_return_1():
    # Arrange
    intervals = [[0, 30], [5, 10], [15, 20]]

    # Act
    result = Solution().minMeetingRooms(intervals)

    # Assert
    assert result == 2


def test_when_example2_then_return_1():
    # Arrange
    intervals = [[7, 10], [2, 4]]

    # Act
    result = Solution().minMeetingRooms(intervals)

    # Assert
    assert result == 1


def test_when_example3_then_return_1():
    # Arrange
    intervals = [[13, 15], [1, 13]]

    # Act
    result = Solution().minMeetingRooms(intervals)

    # Assert
    assert result == 1
