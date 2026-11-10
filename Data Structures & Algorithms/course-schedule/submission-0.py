class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        g = defaultdict(list)

        for x in prerequisites:
            g[x[0]].append(x[1])

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [0] * numCourses

        def dfs(i):
            if states[i] == VISITED:
                return True
            if states[i] == VISITING:
                return False

            states[i] = VISITING

            for neighbor in g[i]:
                if not dfs(neighbor):
                    return False

            states[i] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        