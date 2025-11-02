from collections import defaultdict

WHITE = 0
GRAY = 1
BLACK = 2


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        color_nodes: dict[int, int] = {c: WHITE for c in range(numCourses)}
        graph = self.create_graph(prerequisites)
        order: list[int] = []
        has_cycle = False

        def dfs(node: int):
            nonlocal has_cycle

            color_nodes[node] = GRAY
            for nei in graph[node]:
                if color_nodes[nei] == GRAY:
                    has_cycle = True
                    return

                if color_nodes[nei] == WHITE:
                    dfs(nei)
                    if has_cycle:
                        return

            color_nodes[node] = BLACK
            order.append(node)

        for node, color in color_nodes.items():
            if color == WHITE:
                dfs(node)
                if has_cycle:
                    return []

        order.reverse()
        return order if order else []

    def create_graph(self, prerequisites: list[list[int]]) -> dict[int, list[int]]:
        graph: dict[int, list[int]] = defaultdict(list)

        for p in prerequisites:
            from_node = p[1]
            to_node = p[0]

            graph[from_node].append(to_node)

        return graph
