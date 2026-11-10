class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                    0 <= x < m and 0 <= y < n
                    and (x, y) not in visited
                    and heights[x][y] >= heights[r][c]
                ):
                    dfs(x, y, visited)

        for i in range(m):
            dfs(i, 0, pacific)     
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        return [[r, c] for (r, c) in pacific & atlantic]
                    


        
    