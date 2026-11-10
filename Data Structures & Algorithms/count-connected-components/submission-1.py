class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        g = defaultdict(list)

        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])

        visited = set()
        count = 0
        def dfs(node, parent=None):
            if node in visited:
                return False

            visited.add(node)
            for nei in g[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
            
            return True
        count = 0
        for i in range(n):
            if dfs(i):
                count+=1
        
        return count


            