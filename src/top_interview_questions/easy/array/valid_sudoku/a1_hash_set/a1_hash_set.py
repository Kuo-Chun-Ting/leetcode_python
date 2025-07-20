class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_dict: dict[int, set[str]] = {}
        column_dict: dict[int, set[str]] = {}
        box_dict: dict[int, set[str]] = {}

        for i in range(9):
            row_dict[i] = set()
            column_dict[i] = set()
            box_dict[i] = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if board[i][j] == ".":
                    continue

                # validate row
                if val in row_dict[i]:
                    return False
                row_dict[i].add(val)

                # validate column
                if val in column_dict[j]:
                    return False
                column_dict[j].add(val)

                # validate box
                box_idx = (i // 3) * 3 + j // 3
                if val in box_dict[box_idx]:
                    return False
                box_dict[box_idx].add(val)

        return True
