from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        graph = self.create_graph(equations, values)
        result: list[float] = []
        for query in queries:
            answer = self.dfs(query[0], query[1], graph)
            result.append(answer)
        return result

    def dfs(
        self, start: str, target: str, graph: dict[str, list[tuple[str, float]]]
    ) -> float:
        if start not in graph or target not in graph:
            return -1

        visited: set[str] = set()
        stack: list[tuple[str, float]] = [(start, 1)]
        while stack:
            curr, acc = stack.pop()
            if curr in visited:
                continue

            if curr == target:
                return acc
            visited.add(curr)

            for nei, weight in graph[curr]:
                if nei not in visited:
                    stack.append((nei, acc * weight))

        return -1

    def create_graph(
        self, equations: list[list[str]], values: list[float]
    ) -> dict[str, list[tuple[str, float]]]:
        graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
        for (x, y), v in zip(equations, values):
            graph[x].append((y, v))
            graph[y].append((x, 1 / v))
        return graph
