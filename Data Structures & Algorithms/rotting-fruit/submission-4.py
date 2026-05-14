from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        rotten:List[(int,int)]=[]
        mins = [[float('inf')] * cols for _ in range(rows)]
        self.ans = 0

        def bfs(L:List[(int,int)]):
            q = deque(L)
            visited = set(L)
            
            while q:
                i, j = q.popleft()

                dirs = [(1,0), (-1,0), (0,1), (0,-1)]

                for di, dj in dirs:
                    ni, nj = i + di, j + dj

                    if (
                        0 <= ni < rows and
                        0 <= nj < cols and
                        (ni, nj) not in visited and
                        grid[ni][nj] == 1
                    ):
                        q.append((ni, nj))
                        visited.add((ni, nj))

                        mins[ni][nj] = min(mins[ni][nj], mins[i][j] + 1)
                        self.ans = max(self.ans, mins[ni][nj])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    mins[i][j] = 0
                    rotten.append((i,j))
        bfs(rotten)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and mins[i][j] == float('inf'):
                    return -1

        return self.ans