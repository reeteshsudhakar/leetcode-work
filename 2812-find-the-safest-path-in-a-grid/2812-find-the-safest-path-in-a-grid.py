import heapq

class Solution:
    def compute_safeness_scores(self, grid: List[List[int]], score: List[List[int]], n: int):
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]: # thief
                    score[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            s = score[x][y]

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x = x + dx
                new_y = y + dy
                
                # calculating scores for surrounding cells
                if 0 <= new_x < n and 0 <= new_y < n and score[new_x][new_y] > s + 1:
                    score[new_x][new_y] = s + 1
                    q.append((new_x, new_y))

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] or grid[n - 1][n - 1]: return 0

        score = [[float('inf')] * n for _ in range(n)]
        self.compute_safeness_scores(grid, score, n)

        visited = [[False] * n for _ in range(n)]
        pq = []
        pq.append((-score[0][0], 0, 0))
        
        heapq.heapify(pq)

        while pq:
            safe, x, y = heapq.heappop(pq)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe

            visited[x][y] = True

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                    new_safe = min(safe, score[new_x][new_y])
                    heapq.heappush(pq, (-new_safe, new_x, new_y))
                    visited[new_x][new_y] = True

        return -1
