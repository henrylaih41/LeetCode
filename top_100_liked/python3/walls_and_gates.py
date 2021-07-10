from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n, m = len(rooms[0]), len(rooms)
        visited = [[0]*n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if(rooms[i][j] == 0):
                    queue.append((i, j, 0)) ### (i, j, distance)
                    visited[i][j] = 1
                if(rooms[i][j] == -1):
                    visited[i][j] = 1
        dirr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while(len(queue)):
            i, j, d = queue.popleft()
            for di, dj in dirr:
                if(i+di >= m or i+di < 0 or j+dj >= n or j+dj < 0):
                    continue
                if(not visited[i+di][j+dj]):
                    queue.append((i+di, j+dj, d+1))
                    rooms[i+di][j+dj] = d+1
                    visited[i+di][j+dj] = 1
