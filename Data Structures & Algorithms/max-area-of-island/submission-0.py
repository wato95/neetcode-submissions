class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        check = deque()
        res = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if tuple([row, col]) not in visited:
                        check.append([row, col])
                        count = 0
                        while check:
                            nx, ny = check.pop()
                            if tuple([nx, ny]) not in visited:
                                visited.add(tuple([nx, ny]))
                                count += 1
                                if nx - 1 >= 0:
                                    if grid[nx-1][ny] == 1:
                                        check.append([nx-1, ny])

                                if ny - 1 >= 0:
                                    if grid[nx][ny-1] == 1:
                                        check.append([nx, ny-1])

                                if nx + 1 < len(grid):
                                    if grid[nx+1][ny] == 1:
                                        check.append([nx+1, ny])

                                if ny + 1 < len(grid[0]):
                                    if grid[nx][ny+1] == 1:
                                        check.append([nx, ny+1])
                        res = max(res, count) 

        return res