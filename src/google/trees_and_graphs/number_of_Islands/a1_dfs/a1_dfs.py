class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs((i, j), grid)
        return count

    def dfs(self, start: tuple[int, int], grid: list[list[str]]) -> None:
        m = len(grid)
        n = len(grid[0])
        visited_nodes: set[tuple[int, int]] = set()
        stack: list[tuple[int, int]] = [start]

        while stack:
            node = stack.pop()
            if node in visited_nodes:
                continue

            visited_nodes.add(node)
            i, j = node[0], node[1]
            grid[i][j] = "0"

            top = (i - 1, j) if i - 1 >= 0 else None
            down = (i + 1, j) if i + 1 < m else None
            left = (i, j - 1) if j - 1 >= 0 else None
            right = (i, j + 1) if j + 1 < n else None

            if top and grid[top[0]][top[1]] == "1":
                stack.append((top[0], top[1]))
            if down and grid[down[0]][down[1]] == "1":
                stack.append((down[0], down[1]))
            if right and grid[right[0]][right[1]] == "1":
                stack.append((right[0], right[1]))
            if left and grid[left[0]][left[1]] == "1":
                stack.append((left[0], left[1]))
        return
