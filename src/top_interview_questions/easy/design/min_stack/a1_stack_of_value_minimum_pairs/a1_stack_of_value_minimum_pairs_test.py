from .a1_stack_of_value_minimum_pairs import MinStack


def test_when_example1_then_result_should_be_expected():
    # Arrange
    stack = MinStack()

    # Act
    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    # Assert
    assert stack.getMin() == -3
    assert stack.pop() is None
    assert stack.top() == 0
    assert stack.getMin() == -2
