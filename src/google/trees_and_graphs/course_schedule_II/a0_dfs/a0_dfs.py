from collections import defaultdict

WHITE, GRAY, BLACK = 0, 1, 2


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adjacency_list = self.create_adjacency_list(prerequisites)
        course_status: list[int] = [WHITE] * numCourses
        has_cycle = False
        result: list[int] = []

        def dfs(
            course: int,
        ):
            nonlocal has_cycle
            if course_status[course] == BLACK:
                return

            if course_status[course] == GRAY:
                has_cycle = True
                return

            course_status[course] = GRAY
            for nei in adjacency_list[course]:
                if course_status[nei] == GRAY:
                    has_cycle = True
                    return
                elif course_status[nei] == WHITE:
                    dfs(nei)

            course_status[course] = BLACK
            result.append(course)

        for course in range(numCourses):
            if course_status[course] == WHITE:
                dfs(course)
                if has_cycle:
                    return []

        result.reverse()
        return result

    def create_adjacency_list(
        self, prerequisites: list[list[int]]
    ) -> dict[int, list[int]]:
        adj_list: dict[int, list[int]] = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        return adj_list
