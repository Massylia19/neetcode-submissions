class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #voisins: pour une case quels voisins sont valides
        if not grid: 
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    queue = deque([(r, c)])
                    visited.add((r, c))

                    while queue: 
                        cr,cc = queue.popleft()

                        directions = [(cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)] #(row, column)
                        for (nr, nc) in directions: 
                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == "1" and (nr, nc) not in visited:
                                    visited.add((nr, nc)) 
                                    queue.append((nr, nc)) 

        return count         