class MinStack:

    def __init__(self):
        self._stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        if not self._stack:
            self._stack.append((val, val))
            return

        curr_min = self._stack[-1][0]
        self._stack.append((min(curr_min, val), val))

    def pop(self) -> None:
        min_val, val = self._stack.pop()

    def top(self) -> int:
        min_val, val = self._stack[-1]
        return val

    def getMin(self) -> int:
        min_val, val = self._stack[-1]
        return min_val
