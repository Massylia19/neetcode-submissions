class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {i: [] for i in range(n)}

        for sommet, voisin in edges: 
            adj[sommet].append(voisin)
            adj[voisin].append(sommet)
        
        def dfs(node): 
            visited.add(node)
            for neighbors in adj[node]:
                if neighbors not in visited: 
                    dfs(neighbors)

        number_graphs = 0
        for i in range(n):
            if i not in visited: 
                number_graphs += 1 
                dfs(i)
                
        return number_graphs
        


        

