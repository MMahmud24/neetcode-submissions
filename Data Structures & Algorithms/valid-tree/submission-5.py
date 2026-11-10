class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        g = defaultdict(list)

        for x in edges:
            g[x[0]].append(x[1])
            g[x[1]].append(x[0])

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in g[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

                
            return True
        
        return dfs(0,-1) and len(visited) == n
            

